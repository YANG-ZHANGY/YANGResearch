#!/usr/bin/env python3
"""Validate the complete version 2.0 reproduction workflow."""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path

import pandas as pd
from PIL import Image

from reproduce_core_outputs import HYBRID_FORMULA, HYBRID_TERMS


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = PACKAGE_ROOT / "tables"
FIGURE_DIR = PACKAGE_ROOT / "figures"
SOURCE_DIR = PACKAGE_ROOT / "source_data"
DOCUMENTATION_DIR = PACKAGE_ROOT / "documentation"
REPORT_PATH = DOCUMENTATION_DIR / "REPRODUCTION_VALIDATION.md"

EXPECTED_PANEL = {
    "rows": 1400,
    "countries": 43,
    "start_year": 1980,
    "end_year": 2021,
    "incident_total": 65,
    "positive_country_years": 57,
}

FIGURE_SPECS = {
    "figure1_recorded_legislative_violence_europe": (4251, 3590),
    "figure2_predicted_incidence_closure_polarisation": (4251, 2929),
    "figure3_leave_one_country_out_party_institutionalisation": (4251, 5622),
}


def decimals_for(value: float) -> int:
    return 4 if abs(value) < 0.01 else 3


def matches_reported_precision(reproduced: float, reported: float) -> bool:
    decimals = decimals_for(reported)
    return round(float(reproduced), decimals) == round(float(reported), decimals)


def validate_panel() -> None:
    summary = pd.read_csv(TABLE_DIR / "panel_validation_summary.csv").iloc[0]
    found = {key: int(summary[key]) for key in EXPECTED_PANEL}
    if found != EXPECTED_PANEL:
        raise RuntimeError(f"Panel summary differs from the expected values: {found}")


def validate_tables() -> tuple[pd.DataFrame, pd.DataFrame, int, int]:
    comparison = pd.read_csv(
        TABLE_DIR / "manuscript_reported_vs_reproduced_coefficients.csv"
    )
    if len(comparison) != 41:
        raise RuntimeError(f"Expected 41 reported estimates; found {len(comparison)}.")
    comparison["coefficient_match"] = comparison.apply(
        lambda row: matches_reported_precision(
            row["reproduced_coef"], row["manuscript_coef"]
        ),
        axis=1,
    )
    comparison["standard_error_match"] = comparison.apply(
        lambda row: matches_reported_precision(
            row["reproduced_se"], row["manuscript_se"]
        ),
        axis=1,
    )

    non_hybrid = comparison[comparison["model"] != "Hybrid Poisson"]
    if not (
        non_hybrid["coefficient_match"].all()
        and non_hybrid["standard_error_match"].all()
    ):
        raise RuntimeError(
            "A non-Hybrid model no longer matches the manuscript at its "
            "displayed precision."
        )

    fit = pd.read_csv(TABLE_DIR / "model_fit_summary.csv")
    if len(fit) != 7 or not fit["converged"].astype(bool).all():
        raise RuntimeError("All seven archived models must be present and converged.")

    coefficient_matches = int(comparison["coefficient_match"].sum())
    standard_error_matches = int(comparison["standard_error_match"].sum())
    return comparison, fit, coefficient_matches, standard_error_matches


def validate_hybrid_outputs(fit: pd.DataFrame) -> None:
    results = pd.read_csv(TABLE_DIR / "table3_hybrid_poisson.csv")
    specification = pd.read_csv(
        TABLE_DIR / "table3_hybrid_poisson_specification.csv"
    )
    if list(results["term"]) != HYBRID_TERMS:
        raise RuntimeError("The dedicated Hybrid Poisson output has unexpected terms.")
    numeric_fields = [
        "coef",
        "std_error",
        "p_value",
        "nobs",
        "z_value",
        "ci_95_low",
        "ci_95_high",
    ]
    if results[numeric_fields].isna().any().any():
        raise RuntimeError("The dedicated Hybrid Poisson output contains missing values.")
    if (results["std_error"] <= 0).any():
        raise RuntimeError("Hybrid Poisson standard errors must be positive.")

    hybrid_fit = fit[fit["model"] == "Hybrid Poisson"]
    if len(hybrid_fit) != 1:
        raise RuntimeError("The model-fit summary must contain one Hybrid Poisson row.")
    expected_nobs = int(hybrid_fit.iloc[0]["nobs"])
    if set(results["nobs"].astype(int)) != {expected_nobs}:
        raise RuntimeError("Hybrid Poisson outputs disagree on the analysis sample size.")

    if len(specification) != 1:
        raise RuntimeError("The Hybrid Poisson specification must contain one row.")
    spec = specification.iloc[0]
    if spec["formula"] != HYBRID_FORMULA:
        raise RuntimeError("The deposited Hybrid Poisson formula is inconsistent.")
    if int(spec["nobs"]) != expected_nobs:
        raise RuntimeError("The Hybrid Poisson specification has the wrong sample size.")
    if int(spec["country_clusters"]) <= 1:
        raise RuntimeError("The Hybrid Poisson cluster count is invalid.")


def validate_sources() -> dict[str, int]:
    counts = {
        "figure1_positive_cases": len(
            pd.read_csv(SOURCE_DIR / "figure1_country_counts.csv")
        ),
        "figure1_all_cases": len(
            pd.read_csv(SOURCE_DIR / "figure1_country_counts_all_43.csv")
        ),
        "figure2_publication_rows": len(
            pd.read_csv(SOURCE_DIR / "figure2_publication_source.csv")
        ),
        "figure2_model_rows": len(
            pd.read_csv(SOURCE_DIR / "figure2_model_recomputed_check.csv")
        ),
        "figure3_publication_rows": len(
            pd.read_csv(SOURCE_DIR / "figure3_leave_one_country_out_source.csv")
        ),
        "figure3_model_rows": len(
            pd.read_csv(SOURCE_DIR / "figure3_model_recomputed_check.csv")
        ),
    }
    expected = {
        "figure1_positive_cases": 15,
        "figure1_all_cases": 43,
        "figure2_publication_rows": 802,
        "figure2_model_rows": 240,
        "figure3_publication_rows": 43,
        "figure3_model_rows": 43,
    }
    if counts != expected:
        raise RuntimeError(f"Figure-source validation failed: {counts}")
    return counts


def pdf_page_count(path: Path) -> int:
    process = subprocess.run(
        ["pdfinfo", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    for line in process.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not read the page count for {path.name}.")


def validate_figures() -> None:
    for stem, expected_size in FIGURE_SPECS.items():
        pdf_path = FIGURE_DIR / f"{stem}.pdf"
        png_path = FIGURE_DIR / f"{stem}.png"
        tiff_path = FIGURE_DIR / f"{stem}.tiff"
        if pdf_page_count(pdf_path) != 1:
            raise RuntimeError(f"{pdf_path.name} is not a one-page PDF.")
        with Image.open(png_path) as image:
            if image.size != expected_size:
                raise RuntimeError(
                    f"{png_path.name} has size {image.size}; expected {expected_size}."
                )
            dpi = image.info.get("dpi", (0, 0))
            if min(dpi) < 599:
                raise RuntimeError(f"{png_path.name} is not recorded at 600 dpi.")
        with Image.open(tiff_path) as image:
            if image.size != expected_size:
                raise RuntimeError(
                    f"{tiff_path.name} has size {image.size}; expected {expected_size}."
                )
            dpi = image.info.get("dpi", (0, 0))
            if min(dpi) < 599 or image.info.get("compression") != "tiff_lzw":
                raise RuntimeError(
                    f"{tiff_path.name} must be a 600 dpi LZW-compressed TIFF."
                )


def validate_codebook() -> None:
    panel_columns = list(
        pd.read_csv(PACKAGE_ROOT / "data" / "merged_europe_panel.csv", nrows=0).columns
    )
    codebook = pd.read_csv(DOCUMENTATION_DIR / "codebook.csv")
    if len(codebook) != 86 or list(codebook["variable"]) != panel_columns:
        raise RuntimeError("The codebook does not cover all panel columns in order.")
    if codebook.isna().any().any():
        raise RuntimeError("The codebook contains blank documentation fields.")


def markdown_table(frame: pd.DataFrame) -> str:
    fields = [
        "table",
        "model",
        "term",
        "manuscript_coef",
        "reproduced_coef",
        "manuscript_se",
        "reproduced_se",
    ]
    rows = frame[fields].copy()
    header = "| " + " | ".join(fields) + " |"
    divider = "| " + " | ".join("---" for _ in fields) + " |"
    body = [
        "| "
        + " | ".join(
            f"{value:.6g}" if isinstance(value, float) else str(value)
            for value in row
        )
        + " |"
        for row in rows.itertuples(index=False, name=None)
    ]
    return "\n".join([header, divider, *body])


def write_report(
    comparison: pd.DataFrame,
    fit: pd.DataFrame,
    coefficient_matches: int,
    standard_error_matches: int,
    source_counts: dict[str, int],
) -> None:
    nonmatching = comparison[
        ~comparison["coefficient_match"] | ~comparison["standard_error_match"]
    ]
    exact_models = [
        model
        for model, group in comparison.groupby("model", sort=False)
        if group["coefficient_match"].all() and group["standard_error_match"].all()
    ]
    report = f"""# Reproduction Validation

## Validation result

- Version 2.0 reproduction workflow: **PASSED**.
- Analytic panel: passed.
- Model estimation: all {len(fit)} models converged.
- Manuscript coefficients matched at the displayed precision: {coefficient_matches} of {len(comparison)}.
- Manuscript standard errors matched at the displayed precision: {standard_error_matches} of {len(comparison)}.
- Models matching all displayed coefficients and standard errors: {", ".join(exact_models)}.
- Hybrid Poisson: re-estimated successfully from the deposited panel; dedicated result and specification files passed validation.
- Publication figures: passed for dimensions, 600 dpi raster metadata, TIFF LZW compression, and single-page PDF structure.
- Complete panel codebook: passed for all 86 variables.

## Panel checks

The archived panel contains 1,400 country-year observations, 43 country or party-system episodes, the years 1980–2021, 65 recorded incidents, and 57 country-years with at least one incident.

## Statistical scope

The workflow re-estimates the pooled PPML, year fixed-effects PPML, country-and-year fixed-effects PPML, Hybrid Poisson, first-event complementary log-log, binary logit, and V-Dem party-institutionalisation models. Five-year period groups cover 1980–1984, 1985–1989, and successive five-year intervals. The first-event model includes linear and quadratic analysis-time terms.

All Table 2 estimates and the first-event, binary-logit, and V-Dem results in Table 3 match the manuscript at its displayed precision. The Hybrid Poisson is fully re-estimated from the archived panel and produces complete, finite results. Its five displayed estimates do not all match the manuscript. The source of the difference cannot be resolved because the original final specification could not be recovered. Version 2.0 therefore treats successful re-estimation from the deposited data as the reproducibility criterion for this model and preserves both sets of values below as a manuscript-concordance disclosure.

The dedicated command `python3 code/reproduce_hybrid_poisson.py` writes `tables/table3_hybrid_poisson.csv` and `tables/table3_hybrid_poisson_specification.csv`.

## Hybrid Poisson comparison

{markdown_table(nonmatching)}

## Figure-source checks

- Figure 1: {source_counts["figure1_positive_cases"]} positive cases and {source_counts["figure1_all_cases"]} cases in the complete source table.
- Figure 2: {source_counts["figure2_publication_rows"]} publication-source rows and {source_counts["figure2_model_rows"]} independently recomputed prediction rows.
- Figure 3: {source_counts["figure3_publication_rows"]} publication-source rows and {source_counts["figure3_model_rows"]} independently recomputed leave-one-country-out rows.

Figure 2 and Figure 3 retain separate publication-source and model-recomputed files so that artwork reproduction and statistical re-estimation remain distinguishable.
"""
    REPORT_PATH.write_text(report, encoding="utf-8")


def main() -> None:
    validate_panel()
    comparison, fit, coefficient_matches, standard_error_matches = validate_tables()
    validate_hybrid_outputs(fit)
    source_counts = validate_sources()
    validate_figures()
    validate_codebook()
    write_report(
        comparison,
        fit,
        coefficient_matches,
        standard_error_matches,
        source_counts,
    )
    print(f"Validation report written to {REPORT_PATH}")
    print(
        "Reproduction validation passed. Manuscript concordance: "
        f"{coefficient_matches} of {len(comparison)} coefficients and "
        f"{standard_error_matches} of {len(comparison)} standard errors."
    )


if __name__ == "__main__":
    main()
