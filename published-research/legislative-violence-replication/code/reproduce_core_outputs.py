"""Reproduce core outputs for the JLS legislative violence manuscript.

This script starts from the archived analytic panel included in this
replication package. It does not rebuild the panel from upstream public
datasets. Run it from either the code directory or the package root:

    python code/reproduce_core_outputs.py
"""

from __future__ import annotations

import math
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PACKAGE_ROOT / "data" / "merged_europe_panel.csv"
TABLE_DIR = PACKAGE_ROOT / "tables"
FIGURE_DIR = PACKAGE_ROOT / "figures"
SOURCE_DIR = PACKAGE_ROOT / "source_data"

TABLE_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)
SOURCE_DIR.mkdir(parents=True, exist_ok=True)


TERMS_MAIN = [
    "pi_z",
    "closure_c",
    "closure_sq",
    "pol_c",
    "closure_c:pol_c",
    "log10_gdp",
    "enpp",
    "lsq",
]

HYBRID_TERMS = [
    "pi_between",
    "pi_within",
    "closure_within",
    "closure_within_sq",
    "closure_within:pol_c",
]

HYBRID_FORMULA = (
    "count ~ pi_between + pi_within + closure_within + closure_within_sq "
    "+ closure_within:pol_c + log10_gdp + enpp + lsq + C(year_bin)"
)

LABELS = {
    "pi_z": "Party institutionalisation",
    "pi_between": "PI between-country",
    "pi_within": "PI within-country",
    "v2xps_party": "V-Dem party institutionalisation",
    "closure_c": "Closure (centred)",
    "closure_sq": "Closure^2",
    "pol_c": "Polarisation (centred)",
    "closure_c:pol_c": "Closure x polarisation",
    "closure_within": "Closure within-country",
    "closure_within_sq": "Closure within-country^2",
    "closure_within:pol_c": "Closure x polarisation within",
    "log10_gdp": "Logged GDP per capita",
    "enpp": "Effective number of parties",
    "lsq": "Disproportionality (LSq)",
}


MANUSCRIPT_VALUES = {
    ("Table 2", "Pooled PPML", "pi_z"): (-1.260, 0.178),
    ("Table 2", "Pooled PPML", "closure_c"): (-0.021, 0.015),
    ("Table 2", "Pooled PPML", "closure_sq"): (-0.0009, 0.0004),
    ("Table 2", "Pooled PPML", "pol_c"): (-0.0068, 0.013),
    ("Table 2", "Pooled PPML", "closure_c:pol_c"): (-0.0013, 0.0003),
    ("Table 2", "Pooled PPML", "log10_gdp"): (-3.704, 1.170),
    ("Table 2", "Pooled PPML", "enpp"): (-0.062, 0.082),
    ("Table 2", "Pooled PPML", "lsq"): (-0.032, 0.022),
    ("Table 2", "Year FE PPML", "pi_z"): (-1.348, 0.170),
    ("Table 2", "Year FE PPML", "closure_c"): (-0.020, 0.015),
    ("Table 2", "Year FE PPML", "closure_sq"): (-0.0010, 0.0004),
    ("Table 2", "Year FE PPML", "pol_c"): (-0.0089, 0.015),
    ("Table 2", "Year FE PPML", "closure_c:pol_c"): (-0.0013, 0.0004),
    ("Table 2", "Year FE PPML", "log10_gdp"): (-3.849, 1.324),
    ("Table 2", "Year FE PPML", "enpp"): (-0.045, 0.093),
    ("Table 2", "Year FE PPML", "lsq"): (-0.036, 0.023),
    ("Table 2", "Country + Year FE PPML", "pi_z"): (-0.363, 0.290),
    ("Table 2", "Country + Year FE PPML", "closure_c"): (-0.014, 0.019),
    ("Table 2", "Country + Year FE PPML", "closure_sq"): (-0.0004, 0.0004),
    ("Table 2", "Country + Year FE PPML", "pol_c"): (-0.024, 0.022),
    ("Table 2", "Country + Year FE PPML", "closure_c:pol_c"): (-0.0008, 0.0004),
    ("Table 2", "Country + Year FE PPML", "log10_gdp"): (2.121, 3.243),
    ("Table 2", "Country + Year FE PPML", "enpp"): (-0.119, 0.072),
    ("Table 2", "Country + Year FE PPML", "lsq"): (-0.050, 0.026),
    ("Table 3", "Hybrid Poisson", "pi_between"): (-2.858, 0.884),
    ("Table 3", "Hybrid Poisson", "pi_within"): (-0.402, 0.276),
    ("Table 3", "Hybrid Poisson", "closure_within"): (-0.028, 0.011),
    ("Table 3", "Hybrid Poisson", "closure_within_sq"): (-0.0011, 0.0006),
    ("Table 3", "Hybrid Poisson", "closure_within:pol_c"): (-0.0012, 0.0005),
    ("Table 3", "First-event cloglog", "pi_z"): (-0.800, 0.419),
    ("Table 3", "First-event cloglog", "closure_c"): (-0.054, 0.029),
    ("Table 3", "First-event cloglog", "closure_sq"): (-0.0026, 0.0009),
    ("Table 3", "First-event cloglog", "closure_c:pol_c"): (-0.0028, 0.0014),
    ("Table 3", "Binary logit", "pi_z"): (-1.325, 0.192),
    ("Table 3", "Binary logit", "closure_c"): (-0.019, 0.017),
    ("Table 3", "Binary logit", "closure_sq"): (-0.0011, 0.0005),
    ("Table 3", "Binary logit", "closure_c:pol_c"): (-0.0017, 0.0005),
    ("Table 3", "V-Dem PI robustness", "v2xps_party"): (-8.021, 3.072),
    ("Table 3", "V-Dem PI robustness", "closure_c"): (-0.028, 0.013),
    ("Table 3", "V-Dem PI robustness", "closure_sq"): (-0.0008, 0.0003),
    ("Table 3", "V-Dem PI robustness", "closure_c:pol_c"): (-0.0009, 0.0003),
}


def stars(pvalue: float) -> str:
    if not np.isfinite(pvalue):
        return ""
    if pvalue < 0.001:
        return "***"
    if pvalue < 0.01:
        return "**"
    if pvalue < 0.05:
        return "*"
    if pvalue < 0.10:
        return "dagger"
    return ""


def format_coef(coef: float, se: float, pvalue: float) -> str:
    star = stars(pvalue)
    if abs(coef) < 0.01:
        coef_s = f"{coef:.4f}"
    else:
        coef_s = f"{coef:.3f}"
    return f"{coef_s}{star} ({se:.3f})"


def load_panel() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    numeric_cols = [
        "year",
        "count",
        "countb",
        "adhominem",
        "poweraffecting",
        "symbolic",
        "policydispute",
        "pi_z",
        "closure",
        "pol",
        "log10_gdp",
        "enpp",
        "lsq",
        "v2xps_party",
        "v2psoppaut",
        "v2cacamps",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def prepare_main(df: pd.DataFrame, extra: list[str] | None = None) -> pd.DataFrame:
    cols = [
        "count",
        "countb",
        "pi_z",
        "closure",
        "pol",
        "log10_gdp",
        "enpp",
        "lsq",
        "iso3",
        "country",
        "year",
    ]
    if extra:
        cols.extend(extra)
    out = df[cols].replace([np.inf, -np.inf], np.nan).dropna().copy()
    out["closure_c"] = out["closure"] - out["closure"].mean()
    out["pol_c"] = out["pol"] - out["pol"].mean()
    out["closure_sq"] = out["closure_c"] ** 2
    out["year_bin"] = ((out["year"] - 1980) // 5).astype("category")
    return out


def cluster_glm(formula: str, data: pd.DataFrame, family: sm.families.Family):
    model = smf.glm(formula=formula, data=data, family=family)
    groups = data.loc[model.data.row_labels, "iso3"]
    return model.fit(cov_type="cluster", cov_kwds={"groups": groups})


def tidy_result(table: str, model_name: str, result, terms: list[str]) -> pd.DataFrame:
    rows = []
    for term in terms:
        if term not in result.params.index:
            continue
        rows.append(
            {
                "table": table,
                "model": model_name,
                "term": term,
                "label": LABELS.get(term, term),
                "coef": result.params[term],
                "std_error": result.bse[term],
                "p_value": result.pvalues[term],
                "formatted": format_coef(result.params[term], result.bse[term], result.pvalues[term]),
                "nobs": int(result.nobs),
            }
        )
    return pd.DataFrame(rows)


def write_table_wide(path: Path, tidy: pd.DataFrame) -> None:
    wide = tidy.pivot(index="label", columns="model", values="formatted")
    order = [LABELS[t] for t in tidy["term"].drop_duplicates() if LABELS.get(t) in wide.index]
    wide = wide.reindex(order)
    wide.to_csv(path)


def descriptive_outputs(df: pd.DataFrame) -> None:
    brawl_types = ["adhominem", "poweraffecting", "symbolic", "policydispute"]
    all_countries = (
        df.groupby(["country", "iso3"], as_index=False)
        .agg(
            **{
                "Ad Hominem": ("adhominem", "sum"),
                "Power-Affecting": ("poweraffecting", "sum"),
                "Symbolic": ("symbolic", "sum"),
                "Policy Dispute": ("policydispute", "sum"),
                "Incidents": ("count", "sum"),
                "Positive Years": ("countb", "sum"),
            }
        )
        .sort_values("country")
    )
    all_countries.to_csv(SOURCE_DIR / "figure1_country_counts_all_43.csv", index=False)
    country = (
        all_countries
        .query("Incidents > 0")
        .sort_values(["Incidents", "Positive Years", "country"], ascending=[False, False, True])
    )
    country.to_csv(TABLE_DIR / "table1_recorded_legislative_violence_by_country.csv", index=False)
    country.to_csv(SOURCE_DIR / "figure1_country_counts.csv", index=False)

    vars_desc = [
        ("Legislative violence count", "count"),
        ("Any legislative violence", "countb"),
        ("Party institutionalisation", "pi_z"),
        ("Party-system closure", "closure"),
        ("Party polarisation", "pol"),
        ("Effective number of parties", "enpp"),
        ("Disproportionality (LSq)", "lsq"),
        ("Logged GDP per capita", "log10_gdp"),
        ("V-Dem party institutionalisation", "v2xps_party"),
        ("Opposition autonomy", "v2psoppaut"),
        ("Antagonistic political camps", "v2cacamps"),
    ]
    rows = []
    for label, var in vars_desc:
        if var not in df.columns:
            continue
        s = pd.to_numeric(df[var], errors="coerce")
        rows.append(
            {
                "Variable": label,
                "N": int(s.notna().sum()),
                "Mean": s.mean(),
                "SD": s.std(),
                "Min": s.min(),
                "Max": s.max(),
            }
        )
    pd.DataFrame(rows).round(3).to_csv(TABLE_DIR / "appendix_a2_descriptive_statistics.csv", index=False)

    coverage = (
        df.groupby("country", as_index=False)
        .agg(
            **{
                "Start Year": ("year", "min"),
                "End Year": ("year", "max"),
                "Positive Years": ("countb", "sum"),
                "Incidents": ("count", "sum"),
            }
        )
        .sort_values("country")
    )
    coverage.to_csv(TABLE_DIR / "appendix_a3_country_coverage_positive_years.csv", index=False)


def table2_models(main: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    base = "count ~ pi_z + closure_c + closure_sq + pol_c + closure_c:pol_c + log10_gdp + enpp + lsq"
    specs = {
        "Pooled PPML": base + " + C(year_bin)",
        "Year FE PPML": base + " + C(year)",
        "Country + Year FE PPML": base + " + C(year) + C(iso3)",
    }
    pieces = []
    results = {}
    for name, formula in specs.items():
        res = cluster_glm(formula, main, sm.families.Poisson())
        results[name] = res
        pieces.append(tidy_result("Table 2", name, res, TERMS_MAIN))
    tidy = pd.concat(pieces, ignore_index=True)
    tidy.to_csv(TABLE_DIR / "table2_main_ppml_models_tidy.csv", index=False)
    write_table_wide(TABLE_DIR / "table2_main_ppml_models.csv", tidy)
    return tidy, results


def fit_hybrid_poisson(main: pd.DataFrame) -> tuple[pd.DataFrame, object]:
    """Fit the archived-panel reconstruction of the hybrid Poisson model."""
    hybrid = main.copy()
    hybrid["pi_between"] = hybrid.groupby("iso3")["pi_z"].transform("mean")
    hybrid["pi_within"] = hybrid["pi_z"] - hybrid["pi_between"]
    hybrid["closure_between"] = hybrid.groupby("iso3")["closure"].transform("mean")
    hybrid["closure_within"] = hybrid["closure"] - hybrid["closure_between"]
    hybrid["closure_within_sq"] = hybrid["closure_within"] ** 2
    result = cluster_glm(HYBRID_FORMULA, hybrid, sm.families.Poisson())
    return hybrid, result


def write_hybrid_outputs(hybrid: pd.DataFrame, result) -> None:
    """Write a dedicated, machine-readable Hybrid Poisson result and specification."""
    tidy = tidy_result(
        "Table 3",
        "Hybrid Poisson",
        result,
        HYBRID_TERMS,
    )
    intervals = result.conf_int()
    tidy["z_value"] = tidy["term"].map(result.tvalues)
    tidy["ci_95_low"] = tidy["term"].map(intervals[0])
    tidy["ci_95_high"] = tidy["term"].map(intervals[1])
    tidy.to_csv(TABLE_DIR / "table3_hybrid_poisson.csv", index=False)

    specification = pd.DataFrame(
        [
            {
                "model": "Hybrid Poisson",
                "status": "archived-panel reconstruction",
                "input_file": DATA_PATH.relative_to(PACKAGE_ROOT).as_posix(),
                "formula": HYBRID_FORMULA,
                "family": "Poisson",
                "covariance_type": result.cov_type,
                "cluster_variable": "iso3",
                "nobs": int(result.nobs),
                "country_clusters": int(hybrid.loc[result.model.data.row_labels, "iso3"].nunique()),
                "year_grouping": "five-year periods beginning in 1980",
            }
        ]
    )
    specification.to_csv(
        TABLE_DIR / "table3_hybrid_poisson_specification.csv",
        index=False,
    )


def table3_models(main: pd.DataFrame, df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    results = {}
    pieces = []

    # Within-between hybrid Poisson. This reconstructs the manuscript's
    # reported hybrid logic from the archived panel.
    hybrid, res_hybrid = fit_hybrid_poisson(main)
    results["Hybrid Poisson"] = res_hybrid
    pieces.append(
        tidy_result(
            "Table 3",
            "Hybrid Poisson",
            res_hybrid,
            HYBRID_TERMS,
        )
    )
    write_hybrid_outputs(hybrid, res_hybrid)

    # First-recorded-event complementary log-log model.
    risk = main.sort_values(["iso3", "year"]).copy()
    first_year = risk[risk["count"] > 0].groupby("iso3")["year"].min()
    risk["first_year"] = risk["iso3"].map(first_year)
    risk["first_event"] = ((risk["year"] == risk["first_year"]) & risk["first_year"].notna()).astype(int)
    risk = risk[(risk["first_year"].isna()) | (risk["year"] <= risk["first_year"])].copy()
    risk["time_index"] = risk.groupby("iso3").cumcount() + 1
    f_cloglog = (
        "first_event ~ pi_z + closure_c + closure_sq + pol_c + closure_c:pol_c "
        "+ log10_gdp + enpp + lsq + time_index + I(time_index ** 2)"
    )
    res_cloglog = cluster_glm(f_cloglog, risk, sm.families.Binomial(link=sm.families.links.CLogLog()))
    results["First-event cloglog"] = res_cloglog
    pieces.append(tidy_result("Table 3", "First-event cloglog", res_cloglog, TERMS_MAIN))

    f_logit = (
        "countb ~ pi_z + closure_c + closure_sq + pol_c + closure_c:pol_c "
        "+ log10_gdp + enpp + lsq + C(year_bin)"
    )
    res_logit = cluster_glm(f_logit, main, sm.families.Binomial(link=sm.families.links.Logit()))
    results["Binary logit"] = res_logit
    pieces.append(tidy_result("Table 3", "Binary logit", res_logit, TERMS_MAIN))

    vdem = prepare_main(df, extra=["v2xps_party"])
    f_vdem = (
        "count ~ v2xps_party + closure_c + closure_sq + pol_c + closure_c:pol_c "
        "+ log10_gdp + enpp + lsq + C(year_bin)"
    )
    res_vdem = cluster_glm(f_vdem, vdem, sm.families.Poisson())
    results["V-Dem PI robustness"] = res_vdem
    pieces.append(
        tidy_result(
            "Table 3",
            "V-Dem PI robustness",
            res_vdem,
            ["v2xps_party", "closure_c", "closure_sq", "pol_c", "closure_c:pol_c", "log10_gdp", "enpp", "lsq"],
        )
    )

    tidy = pd.concat(pieces, ignore_index=True)
    tidy.to_csv(TABLE_DIR / "table3_extended_models_tidy.csv", index=False)
    write_table_wide(TABLE_DIR / "table3_extended_models.csv", tidy)
    return tidy, results


def figure2_predictions(main: pd.DataFrame, pooled_result) -> None:
    closure_grid = np.linspace(main["closure"].quantile(0.01), main["closure"].max(), 120)
    low_pol = main["pol"].quantile(0.10)
    high_pol = main["pol"].quantile(0.90)
    closure_mean = main["closure"].mean()
    pol_mean = main["pol"].mean()
    year_bin_mode = main["year_bin"].mode().iloc[0]

    frames = []
    for label, pol_value in [
        ("Lower polarisation (10th pct.)", low_pol),
        ("Higher polarisation (90th pct.)", high_pol),
    ]:
        pred = pd.DataFrame(
            {
                "pi_z": main["pi_z"].mean(),
                "closure": closure_grid,
                "pol": pol_value,
                "log10_gdp": main["log10_gdp"].mean(),
                "enpp": main["enpp"].mean(),
                "lsq": main["lsq"].mean(),
                "year_bin": year_bin_mode,
            }
        )
        pred["closure_c"] = pred["closure"] - closure_mean
        pred["pol_c"] = pred["pol"] - pol_mean
        pred["closure_sq"] = pred["closure_c"] ** 2
        sf = pooled_result.get_prediction(pred).summary_frame()
        pred["mean"] = sf["mean"].to_numpy()
        pred["ci_low"] = sf["mean_ci_lower"].to_numpy()
        pred["ci_high"] = sf["mean_ci_upper"].to_numpy()
        pred["polarisation_level"] = label
        pred["polarisation_percentile"] = 10 if "Lower" in label else 90
        pred["mean_closure_reference"] = closure_mean
        frames.append(pred)
    out = pd.concat(frames, ignore_index=True)
    out.to_csv(SOURCE_DIR / "figure2_model_recomputed_check.csv", index=False)


def figure3_leave_one_out(main: pd.DataFrame) -> None:
    rows = []
    base_formula = (
        "count ~ pi_z + closure_c + closure_sq + pol_c + closure_c:pol_c "
        "+ log10_gdp + enpp + lsq + C(year_bin)"
    )
    full = cluster_glm(base_formula, main, sm.families.Poisson())
    full_coef = full.params["pi_z"]
    for iso3, sub_country in sorted(main[["iso3", "country"]].drop_duplicates().itertuples(index=False)):
        sub = main[main["iso3"] != iso3].copy()
        try:
            res = cluster_glm(base_formula, sub, sm.families.Poisson())
            coef = res.params["pi_z"]
            se = res.bse["pi_z"]
            rows.append(
                {
                    "omitted_iso3": iso3,
                    "omitted_country": sub_country,
                    "coef": coef,
                    "std_error": se,
                    "ci_low": coef - 1.96 * se,
                    "ci_high": coef + 1.96 * se,
                    "full_sample_coef": full_coef,
                }
            )
        except Exception as exc:
            rows.append(
                {
                    "omitted_iso3": iso3,
                    "omitted_country": sub_country,
                    "coef": np.nan,
                    "std_error": np.nan,
                    "ci_low": np.nan,
                    "ci_high": np.nan,
                    "full_sample_coef": full_coef,
                    "error": str(exc),
                }
            )
    out = pd.DataFrame(rows).sort_values("coef")
    out.to_csv(SOURCE_DIR / "figure3_model_recomputed_check.csv", index=False)


def manuscript_comparison(tidy: pd.DataFrame) -> None:
    rows = []
    for (table, model, term), (m_coef, m_se) in MANUSCRIPT_VALUES.items():
        match = tidy[(tidy["table"] == table) & (tidy["model"] == model) & (tidy["term"] == term)]
        if match.empty:
            rows.append(
                {
                    "table": table,
                    "model": model,
                    "term": term,
                    "manuscript_coef": m_coef,
                    "reproduced_coef": np.nan,
                    "coef_difference": np.nan,
                    "manuscript_se": m_se,
                    "reproduced_se": np.nan,
                    "se_difference": np.nan,
                }
            )
            continue
        row = match.iloc[0]
        rows.append(
            {
                "table": table,
                "model": model,
                "term": term,
                "manuscript_coef": m_coef,
                "reproduced_coef": row["coef"],
                "coef_difference": row["coef"] - m_coef,
                "manuscript_se": m_se,
                "reproduced_se": row["std_error"],
                "se_difference": row["std_error"] - m_se,
            }
        )
    pd.DataFrame(rows).to_csv(TABLE_DIR / "manuscript_reported_vs_reproduced_coefficients.csv", index=False)


def write_model_fit_summary(
    table2_results: dict[str, object],
    table3_results: dict[str, object],
) -> None:
    rows = []
    for table, results in [
        ("Table 2", table2_results),
        ("Table 3", table3_results),
    ]:
        for model_name, result in results.items():
            rows.append(
                {
                    "table": table,
                    "model": model_name,
                    "nobs": int(result.nobs),
                    "converged": bool(getattr(result, "converged", True)),
                    "log_likelihood": float(result.llf),
                    "aic": float(result.aic),
                    "deviance": float(result.deviance),
                    "pearson_chi2": float(result.pearson_chi2),
                    "covariance_type": result.cov_type,
                }
            )
    pd.DataFrame(rows).to_csv(TABLE_DIR / "model_fit_summary.csv", index=False)


def write_validation_summary(df: pd.DataFrame) -> None:
    summary = {
        "rows": len(df),
        "countries": df["iso3"].nunique(),
        "start_year": int(df["year"].min()),
        "end_year": int(df["year"].max()),
        "incident_total": int(df["count"].sum()),
        "positive_country_years": int((df["count"] > 0).sum()),
    }
    pd.DataFrame([summary]).to_csv(TABLE_DIR / "panel_validation_summary.csv", index=False)
    expected = {
        "rows": 1400,
        "countries": 43,
        "start_year": 1980,
        "end_year": 2021,
        "incident_total": 65,
        "positive_country_years": 57,
    }
    problems = {k: (summary[k], expected[k]) for k in expected if summary[k] != expected[k]}
    if problems:
        raise RuntimeError(f"Panel validation failed: {problems}")


def main() -> None:
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    df = load_panel()
    write_validation_summary(df)
    descriptive_outputs(df)
    main_df = prepare_main(df)
    table2, table2_results = table2_models(main_df)
    table3, table3_results = table3_models(main_df, df)
    all_tidy = pd.concat([table2, table3], ignore_index=True)
    manuscript_comparison(all_tidy)
    write_model_fit_summary(table2_results, table3_results)
    figure2_predictions(main_df, table2_results["Pooled PPML"])
    figure3_leave_one_out(main_df)
    print("Replication outputs written to:")
    print(f"  {TABLE_DIR}")
    print(f"  {SOURCE_DIR}")


if __name__ == "__main__":
    main()
