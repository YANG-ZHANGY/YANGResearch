#!/usr/bin/env python3
"""Generate a complete variable codebook for the supplied analytic panel."""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PANEL_PATH = PACKAGE_ROOT / "data" / "merged_europe_panel.csv"
OUTPUT_PATH = PACKAGE_ROOT / "documentation" / "codebook.csv"
EXPECTED_COLUMN_COUNT = 86

OUTPUT_COLUMNS = [
    "variable",
    "label",
    "definition",
    "data_type",
    "unit_or_scale",
    "allowed_values",
    "missing_value",
    "source",
    "transformation",
    "notes",
]


def metadata(
    label: str,
    definition: str,
    unit_or_scale: str,
    source: str,
    transformation: str = "No additional transformation is documented in this package.",
    notes: str = "",
) -> dict[str, str]:
    return {
        "label": label,
        "definition": definition,
        "unit_or_scale": unit_or_scale,
        "source": source,
        "transformation": transformation,
        "notes": notes,
    }


BASE_METADATA = {
    "country": metadata(
        "Country episode",
        "Country or party-system episode name used to identify the panel unit.",
        "Text identifier",
        "Who Governs Europe and the merged panel",
        notes="Roman numerals distinguish party-system episodes where present.",
    ),
    "year": metadata(
        "Year",
        "Calendar year of the country-year observation.",
        "Calendar year",
        "Merged panel",
    ),
    "closure": metadata(
        "Party-system closure",
        "Party-system closure score used in the manuscript models.",
        "Index points; observed values lie within 0 to 100",
        "Who Governs Europe and the merged panel",
    ),
    "closure_fl": metadata(
        "Party-system closure, filled series",
        "Filled or smoothed party-system closure series supplied with the merged panel.",
        "Index points; observed values lie within 0 to 100",
        "Who Governs Europe and the merged panel",
        "The fill or smoothing operation occurred before creation of this package.",
        "The exact fill procedure is not restated in the package.",
    ),
    "pi_z": metadata(
        "Party institutionalisation, standardised",
        "Standardised party-institutionalisation score used in the manuscript models.",
        "Standardised index",
        "Who Governs Europe and the merged panel",
        "Standardisation occurred before creation of this package.",
        "The centring and scaling constants are not stored as separate fields.",
    ),
    "alt_fl": metadata(
        "Alternation component, filled series",
        "Filled series for the alternation component stored in the merged panel.",
        "Index points; observed values lie within 0 to 100",
        "Who Governs Europe and the merged panel",
        "The fill operation occurred before creation of this package.",
        "Interpret the component with the cited source documentation.",
    ),
    "form_fl": metadata(
        "Government-formula component, filled series",
        "Filled series for the government-formula component stored in the merged panel.",
        "Index points; observed values lie within 0 to 100",
        "Who Governs Europe and the merged panel",
        "The fill operation occurred before creation of this package.",
        "Interpret the component with the cited source documentation.",
    ),
    "acc_fl": metadata(
        "Access component, filled series",
        "Filled series for the government-access component stored in the merged panel.",
        "Index points; observed values lie within 0 to 100",
        "Who Governs Europe and the merged panel",
        "The fill operation occurred before creation of this package.",
        "Interpret the component with the cited source documentation.",
    ),
    "epd": metadata(
        "EPD measure",
        "Party-system measure stored under the source field name epd.",
        "Source scale as supplied",
        "Who Governs Europe and the merged panel",
        notes="Interpret the field with the cited source documentation.",
    ),
    "aaph": metadata(
        "AAPH measure",
        "Party-system measure stored under the source field name aaph.",
        "Source scale as supplied",
        "Who Governs Europe and the merged panel",
        notes="Interpret the field with the cited source documentation.",
    ),
    "enpp": metadata(
        "Effective number of parties",
        "Effective number of parliamentary parties.",
        "Effective number of parties",
        "Who Governs Europe and the merged panel",
    ),
    "log10_gdp": metadata(
        "Logged GDP per capita",
        "Base-10 logarithm of the GDP-per-capita measure stored in the merged panel.",
        "Base-10 logarithmic units",
        "Merged panel; the upstream economic series is not specified in this package",
        "Base-10 logarithm computed before creation of this package.",
    ),
    "pol": metadata(
        "Party polarisation",
        "Party-system polarisation score used in the manuscript models.",
        "Index points as supplied",
        "Who Governs Europe and the merged panel",
    ),
    "lsq": metadata(
        "Disproportionality",
        "Gallagher least-squares disproportionality score.",
        "Index points",
        "Who Governs Europe and the merged panel",
    ),
    "demyear": metadata(
        "Democratic duration",
        "Democratic-duration field stored in the merged panel.",
        "Years as supplied",
        "Merged panel",
        notes="Interpret the starting rule with the cited source documentation.",
    ),
    "v2xps_party": metadata(
        "V-Dem party institutionalisation",
        "V-Dem party-institutionalisation index used for a robustness model.",
        "V-Dem source scale",
        "V-Dem field v2xps_party as merged into the supplied panel",
    ),
    "tev": metadata(
        "Total electoral volatility",
        "Total-electoral-volatility measure stored in the merged panel.",
        "Index points as supplied",
        "Who Governs Europe and the merged panel",
    ),
    "region1": metadata(
        "European region",
        "Broad European region assigned to the panel unit.",
        "Categorical",
        "Who Governs Europe and the merged panel",
    ),
    "v2psorgs": metadata(
        "V-Dem party-organisation measure",
        "Value stored under the V-Dem source field v2psorgs.",
        "V-Dem source scale",
        "V-Dem field v2psorgs as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2psprlnks": metadata(
        "V-Dem party-linkage measure",
        "Value stored under the V-Dem source field v2psprlnks.",
        "V-Dem source scale",
        "V-Dem field v2psprlnks as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "country_base": metadata(
        "Country name key",
        "Lower-case country-name key used for merging.",
        "Text identifier",
        "Derived in the merged panel",
        "Country names were normalised before creation of this package.",
    ),
    "iso3": metadata(
        "ISO3 country code",
        "Three-letter country code used for merging and country-level clustering.",
        "Three-letter code",
        "FISTS and the merged panel",
    ),
    "cname_year": metadata(
        "Country-year key",
        "Composite country-name and year identifier.",
        "Text identifier",
        "Derived in the merged panel",
        "Country name and year were combined before creation of this package.",
    ),
    "ccode": metadata(
        "ISO numeric country code",
        "Numeric country identifier stored in the merged panel.",
        "Numeric identifier",
        "Merged panel identifiers",
    ),
    "cname": metadata(
        "Country name",
        "Country name without the party-system episode suffix.",
        "Text identifier",
        "Merged panel identifiers",
    ),
    "ccodealp": metadata(
        "Alphabetic country code",
        "Three-letter alphabetic country identifier stored in the merged panel.",
        "Three-letter code",
        "Merged panel identifiers",
    ),
    "ccodealp_year": metadata(
        "Alphabetic country-year code",
        "Composite alphabetic country code and two-digit year identifier.",
        "Text identifier",
        "Derived in the merged panel",
        "Country code and year were combined before creation of this package.",
    ),
    "ccodecow": metadata(
        "Correlates of War country code",
        "Numeric Correlates of War country identifier where supplied.",
        "Numeric identifier",
        "Merged panel identifiers",
    ),
    "adhominem": metadata(
        "Ad hominem incidents",
        "Annual count of recorded ad hominem legislative-violence incidents.",
        "Number of incidents",
        "FISTS / Schmoll and Ting archive merged into the Europe panel",
    ),
    "poweraffecting": metadata(
        "Power-affecting incidents",
        "Annual count of recorded power-affecting legislative-violence incidents.",
        "Number of incidents",
        "FISTS / Schmoll and Ting archive merged into the Europe panel",
    ),
    "symbolic": metadata(
        "Symbolic incidents",
        "Annual count of recorded symbolic legislative-violence incidents.",
        "Number of incidents",
        "FISTS / Schmoll and Ting archive merged into the Europe panel",
    ),
    "policydispute": metadata(
        "Policy-dispute incidents",
        "Annual count of recorded policy-dispute legislative-violence incidents.",
        "Number of incidents",
        "FISTS / Schmoll and Ting archive merged into the Europe panel",
    ),
    "count": metadata(
        "Legislative violence count",
        "Annual number of recorded physical confrontations in the legislature.",
        "Number of incidents",
        "FISTS / Schmoll and Ting archive merged into the Europe panel",
    ),
    "countb": metadata(
        "Any legislative violence",
        "Indicator equal to 1 when the annual incident count is greater than 0 and 0 otherwise.",
        "Binary indicator",
        "Derived from count",
        "Computed as count greater than 0.",
    ),
    "execnat": metadata(
        "Executive-national field",
        "Binary field stored under the source name execnat.",
        "Binary source coding",
        "Merged panel",
        notes="The substantive code labels are not specified in this package.",
    ),
    "yrsoffc": metadata(
        "Years in office",
        "Years-in-office field stored in the merged panel.",
        "Years as supplied",
        "Merged panel",
    ),
    "pr": metadata(
        "PR indicator",
        "Binary electoral-system field stored under the source name pr.",
        "Binary source coding",
        "Merged panel",
        notes="The substantive code labels are not specified in this package.",
    ),
    "system": metadata(
        "Political-system category",
        "Categorical field stored under the source name system.",
        "Integer category",
        "Merged panel",
        notes="The substantive category labels are not specified in this package.",
    ),
    "country_base_clean": metadata(
        "Clean country name key",
        "Normalised lower-case country-name key used for merging.",
        "Text identifier",
        "Derived in the merged panel",
        "Country names were normalised before creation of this package.",
    ),
    "v2lgbicam": metadata(
        "V-Dem legislative-chamber field",
        "Value stored under the V-Dem source field v2lgbicam.",
        "V-Dem source coding",
        "V-Dem field v2lgbicam as merged into the supplied panel",
        notes="Interpret the codes with the cited V-Dem documentation.",
    ),
    "v2xpas_democracy": metadata(
        "V-Dem v2xpas_democracy measure",
        "Value stored under the V-Dem source field v2xpas_democracy.",
        "V-Dem source scale",
        "V-Dem field v2xpas_democracy as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2xpas_democracy_government": metadata(
        "V-Dem v2xpas_democracy_government measure",
        "Value stored under the V-Dem source field v2xpas_democracy_government.",
        "V-Dem source scale",
        "V-Dem field v2xpas_democracy_government as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2x_genpp": metadata(
        "V-Dem v2x_genpp index",
        "Value stored under the V-Dem source field v2x_genpp.",
        "V-Dem source scale",
        "V-Dem field v2x_genpp as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2x_delibdem": metadata(
        "V-Dem deliberative democracy index",
        "V-Dem deliberative-democracy index.",
        "V-Dem source scale",
        "V-Dem field v2x_delibdem as merged into the supplied panel",
    ),
    "v2cacamps": metadata(
        "Antagonistic political camps",
        "V-Dem measure of antagonistic political camps.",
        "V-Dem source scale",
        "V-Dem field v2cacamps as merged into the supplied panel",
    ),
    "v2pscohesv": metadata(
        "V-Dem v2pscohesv measure",
        "Value stored under the V-Dem source field v2pscohesv.",
        "V-Dem source scale",
        "V-Dem field v2pscohesv as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2elrstrct": metadata(
        "V-Dem v2elrstrct indicator",
        "Value stored under the V-Dem source field v2elrstrct.",
        "V-Dem source coding",
        "V-Dem field v2elrstrct as merged into the supplied panel",
        notes="Interpret the codes with the cited V-Dem documentation.",
    ),
    "e_miinterc": metadata(
        "Electoral-system e_miinterc indicator",
        "Value stored under the source field e_miinterc.",
        "Binary source coding",
        "V-Dem country-year data as merged into the supplied panel",
        notes="Interpret the codes with the cited source documentation.",
    ),
    "v2xpas_economic": metadata(
        "V-Dem v2xpas_economic measure",
        "Value stored under the V-Dem source field v2xpas_economic.",
        "V-Dem source scale",
        "V-Dem field v2xpas_economic as merged into the supplied panel",
        notes="Interpret the field with the cited V-Dem documentation.",
    ),
    "v2psoppaut": metadata(
        "Opposition autonomy",
        "V-Dem measure of opposition autonomy.",
        "V-Dem source scale",
        "V-Dem field v2psoppaut as merged into the supplied panel",
    ),
}


def infer_data_type(series: pd.Series) -> str:
    observed = series.dropna()
    if pd.api.types.is_bool_dtype(series):
        return "boolean"
    if pd.api.types.is_numeric_dtype(series):
        if observed.empty:
            return "numeric"
        numeric = pd.to_numeric(observed, errors="coerce").to_numpy(dtype=float)
        if np.isfinite(numeric).all() and np.equal(numeric, np.floor(numeric)).all():
            return "integer"
        return "numeric"
    return "string"


def format_number(value: float | int) -> str:
    number = float(value)
    if number.is_integer():
        return str(int(number))
    return f"{number:.12g}"


def allowed_values(series: pd.Series, data_type: str) -> str:
    observed = series.dropna()
    unique = observed.drop_duplicates()
    if unique.empty:
        return "No observed non-missing values"

    if data_type in {"integer", "numeric", "boolean"}:
        numeric = pd.to_numeric(unique, errors="coerce").dropna()
        if len(numeric) <= 20:
            values = sorted(float(value) for value in numeric)
            return "Observed values: " + "; ".join(format_number(value) for value in values)
        return (
            "Observed range: "
            + format_number(numeric.min())
            + " to "
            + format_number(numeric.max())
        )

    values = sorted(str(value) for value in unique)
    if len(values) <= 20:
        return "Observed values: " + "; ".join(values)
    return f"{len(values)} observed text values; see the data file"


def missing_value_text(series: pd.Series) -> str:
    missing_count = int(series.isna().sum())
    total_count = int(len(series))
    if missing_count == 0:
        return f"No blank/NA values observed in {total_count} rows"
    return f"Blank/NA; {missing_count} of {total_count} rows"


def metadata_for_variable(variable: str) -> dict[str, str]:
    lag_match = re.fullmatch(r"(.+)_lag(\d+)", variable)
    if lag_match:
        base_variable = lag_match.group(1)
        lag_years = int(lag_match.group(2))
        if base_variable not in BASE_METADATA:
            raise KeyError(f"No base metadata found for lagged field: {variable}")
        base = BASE_METADATA[base_variable]
        year_word = "year" if lag_years == 1 else "years"
        return {
            "label": f"{base['label']}, {lag_years}-year lag",
            "definition": (
                f"{base['definition']} This field records the supplied value "
                f"from {lag_years} {year_word} earlier."
            ),
            "unit_or_scale": base["unit_or_scale"],
            "source": base["source"],
            "transformation": (
                f"{lag_years}-year lag of {base_variable}; temporal "
                "alignment is supplied with the panel and is not recomputed here."
            ),
            "notes": (
                f"Metadata inherit from {base_variable}. "
                "Boundary-year coverage follows the supplied panel."
            ),
        }

    if variable not in BASE_METADATA:
        raise KeyError(f"No metadata found for field: {variable}")
    return BASE_METADATA[variable]


def generate_codebook() -> pd.DataFrame:
    panel = pd.read_csv(PANEL_PATH, low_memory=False)
    if len(panel.columns) != EXPECTED_COLUMN_COUNT:
        raise ValueError(
            f"Expected {EXPECTED_COLUMN_COUNT} columns in {PANEL_PATH}, "
            f"found {len(panel.columns)}."
        )
    if panel.columns.duplicated().any():
        duplicates = panel.columns[panel.columns.duplicated()].tolist()
        raise ValueError(f"Duplicate column names found: {duplicates}")

    rows: list[dict[str, object]] = []
    for variable in panel.columns:
        series = panel[variable]
        field_metadata = metadata_for_variable(variable)
        data_type = infer_data_type(series)
        observed_count = int(series.notna().sum())
        distinct_count = int(series.dropna().nunique())
        observation_note = (
            f"Observed non-missing values: {observed_count}; "
            f"distinct observed values: {distinct_count}."
        )
        notes = " ".join(
            part for part in [field_metadata["notes"], observation_note] if part
        )
        rows.append(
            {
                "variable": variable,
                "label": field_metadata["label"],
                "definition": field_metadata["definition"],
                "data_type": data_type,
                "unit_or_scale": field_metadata["unit_or_scale"],
                "allowed_values": allowed_values(series, data_type),
                "missing_value": missing_value_text(series),
                "source": field_metadata["source"],
                "transformation": field_metadata["transformation"],
                "notes": notes,
            }
        )

    codebook = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    if codebook["variable"].tolist() != panel.columns.tolist():
        raise RuntimeError("Codebook column order does not match the panel.")
    return codebook


def main() -> None:
    codebook = generate_codebook()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    codebook.to_csv(OUTPUT_PATH, index=False, encoding="utf-8", lineterminator="\n")
    print(f"Wrote {len(codebook)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
