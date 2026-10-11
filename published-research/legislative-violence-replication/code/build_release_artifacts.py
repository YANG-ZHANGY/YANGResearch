#!/usr/bin/env python3
"""Create release checksums, a file manifest, and an optional stable ZIP."""

from __future__ import annotations

import argparse
import csv
import hashlib
import mimetypes
import os
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PACKAGE_ROOT / "FILE_MANIFEST.csv"
CHECKSUM_PATH = PACKAGE_ROOT / "SHA256SUMS.txt"
COMPARISON_PATH = (
    PACKAGE_ROOT
    / "tables"
    / "manuscript_reported_vs_reproduced_coefficients.csv"
)

MANIFEST_FIELDS = [
    "relative_path",
    "category",
    "description",
    "media_type",
    "size_bytes",
    "sha256",
    "source_or_generated_by",
    "supports_output",
    "license",
]

EXCLUDED_DIRECTORY_NAMES = {
    "__MACOSX",
    "__pycache__",
    "node_modules",
}
EXCLUDED_FILE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    MANIFEST_PATH.name,
    CHECKSUM_PATH.name,
}
EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".swp",
    ".tmp",
    ".zip",
}

MEDIA_TYPE_OVERRIDES = {
    ".cff": "text/yaml",
    ".csv": "text/csv",
    ".geojson": "application/geo+json",
    ".md": "text/markdown",
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".py": "text/x-python",
    ".r": "text/x-r-source",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".txt": "text/plain",
    ".yaml": "text/yaml",
    ".yml": "text/yaml",
}


def is_excluded(relative_path: Path) -> bool:
    if any(part.startswith(".") for part in relative_path.parts):
        return True
    if any(part in EXCLUDED_DIRECTORY_NAMES for part in relative_path.parts[:-1]):
        return True
    if relative_path.name in EXCLUDED_FILE_NAMES:
        return True
    if relative_path.name.startswith("~$"):
        return True
    if relative_path.name.endswith(".zip.sha256"):
        return True
    return relative_path.suffix.lower() in EXCLUDED_SUFFIXES


def collect_payload_files() -> list[Path]:
    files: list[Path] = []
    for path in PACKAGE_ROOT.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative_path = path.relative_to(PACKAGE_ROOT)
        if is_excluded(relative_path):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(PACKAGE_ROOT).as_posix())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def media_type_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in MEDIA_TYPE_OVERRIDES:
        return MEDIA_TYPE_OVERRIDES[suffix]
    guessed, _ = mimetypes.guess_type(path.name)
    return guessed or "application/octet-stream"


def figure_number(name: str) -> str:
    lower_name = name.lower()
    for number in ("1", "2", "3"):
        if f"figure{number}" in lower_name or f"figure_{number}" in lower_name:
            return number
    return ""


def category_for(relative_path: Path) -> str:
    top = relative_path.parts[0] if len(relative_path.parts) > 1 else ""
    mapping = {
        "code": "code",
        "data": "analytic_data",
        "documentation": "documentation",
        "figures": "publication_figure",
        "source_data": "figure_source_data",
        "tables": "reproduced_table",
    }
    return mapping.get(top, "package_documentation")


def description_for(relative_path: Path) -> str:
    name = relative_path.name.lower()
    number = figure_number(name)

    if name == "merged_europe_panel.csv":
        return "Analytic country-year panel used by the reproduction scripts."
    if name == "reproduce_core_outputs.py":
        return "Python script that reproduces model tables and machine-readable outputs."
    if name == "reproduce_hybrid_poisson.py":
        return "Python script that provides a standalone Hybrid Poisson reproduction command."
    if name == "reproduce_all.py":
        return "Python script that runs the complete reproduction and validation workflow."
    if name == "validate_reproduction.py":
        return "Python script that validates model values, figures, sources, and documentation."
    if name == "generate_codebook.py":
        return "Python script that generates the complete panel codebook."
    if name == "build_release_artifacts.py":
        return "Python script that creates release checksums, a file manifest, and a ZIP."
    if name == "render_publication_figures.r":
        return "R script that renders the publication figures."
    if name == "prepare_figure2_source.py":
        return "Python script that prepares the publication source values for Figure 2."
    if name == "png_to_lzw_tiff.py":
        return "Python helper that converts PNG artwork to lossless LZW TIFF."
    if name == "codebook.csv":
        return "Variable-level documentation for every field in the analytic panel."
    if name == "ne_110m_admin_0_countries.geojson":
        return "Country-boundary GeoJSON used to render Figure 1."
    if name == "figure2_publication_source.csv":
        return "Deposited source values that reproduce the accepted Figure 2 artwork."
    if name == "figure2_model_recomputed_check.csv":
        return "Predictions independently recomputed from the archived panel for Figure 2 model checking."
    if name == "figure3_leave_one_country_out_source.csv":
        return "Deposited source values that reproduce the accepted Figure 3 artwork."
    if name == "figure3_model_recomputed_check.csv":
        return "Leave-one-country-out estimates independently recomputed from the archived panel."
    if relative_path.parts and relative_path.parts[0] == "figures" and number:
        return f"Publication artwork for Figure {number}."
    if relative_path.parts and relative_path.parts[0] == "source_data" and number:
        return f"Machine-readable values used for Figure {number}."
    if relative_path.parts and relative_path.parts[0] == "tables":
        return "Machine-readable reproduced table or model summary."
    if relative_path.parts and relative_path.parts[0] == "documentation":
        return "Documentation for package use, interpretation, or citation."
    if relative_path.suffix.lower() in {".md", ".txt", ".cff"}:
        return "Package documentation."
    return "File included in the replication package."


def source_for(relative_path: Path) -> str:
    name = relative_path.name.lower()
    number = figure_number(name)

    if name == "merged_europe_panel.csv":
        return "Supplied analytic panel"
    if name == "ne_110m_admin_0_countries.geojson":
        return "Natural Earth Admin 0 countries data"
    if relative_path.parts and relative_path.parts[0] == "figures":
        return "code/render_publication_figures.R"
    if relative_path.parts and relative_path.parts[0] == "tables":
        return "code/reproduce_core_outputs.py"
    if relative_path.parts and relative_path.parts[0] == "source_data":
        if name in {
            "figure2_publication_source.csv",
            "figure3_leave_one_country_out_source.csv",
        }:
            return "Deposited publication source table"
        if name in {
            "figure2_model_recomputed_check.csv",
            "figure3_model_recomputed_check.csv",
        }:
            return "code/reproduce_core_outputs.py"
        if number == "1":
            return "code/reproduce_core_outputs.py"
        return "Supplied figure source data"
    if name == "codebook.csv":
        return "code/generate_codebook.py"
    if relative_path.parts and relative_path.parts[0] == "code":
        return "Author-supplied release code"
    if relative_path.parts and relative_path.parts[0] == "documentation":
        return "Release documentation"
    return "Package assembly"


def supports_output_for(relative_path: Path) -> str:
    name = relative_path.name.lower()
    number = figure_number(name)

    if name == "figure2_model_recomputed_check.csv":
        return "Figure 2 statistical check"
    if name == "figure3_model_recomputed_check.csv":
        return "Figure 3 statistical check"
    if number:
        return f"Figure {number}"
    if name == "merged_europe_panel.csv":
        return "Model tables, appendix summaries, and figure source values"
    if name == "reproduce_core_outputs.py":
        return "Model tables, appendix summaries, and figure source values"
    if name == "reproduce_hybrid_poisson.py":
        return "Hybrid Poisson result and specification tables"
    if name == "render_publication_figures.r":
        return "Figures 1-3"
    if name == "prepare_figure2_source.py":
        return "Figure 2"
    if name == "ne_110m_admin_0_countries.geojson":
        return "Figure 1"
    if relative_path.parts and relative_path.parts[0] == "tables":
        return relative_path.stem.replace("_", " ")
    if name == "codebook.csv":
        return "Interpretation of the analytic panel"
    if relative_path.parts and relative_path.parts[0] == "documentation":
        return "Package use and interpretation"
    if relative_path.parts and relative_path.parts[0] == "code":
        return "Package regeneration"
    return "Package completeness"


def license_for(relative_path: Path) -> str:
    name = relative_path.name.lower()
    if name == "ne_110m_admin_0_countries.geojson":
        return "Natural Earth public-domain terms"
    if relative_path.parts and relative_path.parts[0] == "data":
        return "See LICENSE.txt and upstream source terms"
    return "See LICENSE.txt"


def build_manifest_rows(payload_files: list[Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in payload_files:
        relative_path = path.relative_to(PACKAGE_ROOT)
        rows.append(
            {
                "relative_path": relative_path.as_posix(),
                "category": category_for(relative_path),
                "description": description_for(relative_path),
                "media_type": media_type_for(path),
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "source_or_generated_by": source_for(relative_path),
                "supports_output": supports_output_for(relative_path),
                "license": license_for(relative_path),
            }
        )
    return rows


def decimals_for(value: float) -> int:
    return 4 if abs(value) < 0.01 else 3


def matches_reported_precision(reproduced: float, reported: float) -> bool:
    decimals = decimals_for(reported)
    return round(reproduced, decimals) == round(reported, decimals)


def statistical_release_gate() -> tuple[int, int, set[str]]:
    if not COMPARISON_PATH.exists():
        raise RuntimeError(
            "Run code/reproduce_core_outputs.py before building release artifacts."
        )
    with COMPARISON_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 41:
        raise RuntimeError(
            f"Expected 41 manuscript comparisons; found {len(rows)}."
        )
    matches = 0
    mismatched_models: set[str] = set()
    for row in rows:
        coefficient_match = matches_reported_precision(
            float(row["reproduced_coef"]),
            float(row["manuscript_coef"]),
        )
        standard_error_match = matches_reported_precision(
            float(row["reproduced_se"]),
            float(row["manuscript_se"]),
        )
        pair_matches = coefficient_match and standard_error_match
        matches += int(pair_matches)
        if not pair_matches:
            mismatched_models.add(row["model"])
    return matches, len(rows), mismatched_models


def write_manifest(rows: list[dict[str, object]]) -> None:
    with MANIFEST_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=MANIFEST_FIELDS,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_checksums(payload_files: list[Path]) -> None:
    checksum_files = sorted(
        [*payload_files, MANIFEST_PATH],
        key=lambda item: item.relative_to(PACKAGE_ROOT).as_posix(),
    )
    with CHECKSUM_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for path in checksum_files:
            relative_path = path.relative_to(PACKAGE_ROOT).as_posix()
            handle.write(f"{sha256_file(path)}  {relative_path}\n")


def validate_archive_root(archive_root: str) -> str:
    cleaned = archive_root.strip("/")
    if not cleaned:
        return ""
    parts = PurePosixPath(cleaned).parts
    if any(part in {"", ".", ".."} or part.startswith(".") for part in parts):
        raise ValueError("Archive root must be a visible relative path.")
    return PurePosixPath(*parts).as_posix()


def archive_name(relative_path: Path, archive_root: str) -> str:
    name = relative_path.as_posix()
    return f"{archive_root}/{name}" if archive_root else name


def create_zip(zip_path: Path, archive_root: str) -> Path:
    archive_root = validate_archive_root(archive_root)
    archive_files = sorted(
        [*collect_payload_files(), MANIFEST_PATH, CHECKSUM_PATH],
        key=lambda item: item.relative_to(PACKAGE_ROOT).as_posix(),
    )

    zip_path = zip_path.expanduser().resolve()
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_handle = tempfile.NamedTemporaryFile(
        prefix=f"{zip_path.name}.",
        suffix=".tmp",
        dir=zip_path.parent,
        delete=False,
    )
    temporary_path = Path(temporary_handle.name)
    temporary_handle.close()

    try:
        with zipfile.ZipFile(
            temporary_path,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            strict_timestamps=True,
        ) as archive:
            for path in archive_files:
                relative_path = path.relative_to(PACKAGE_ROOT)
                info = zipfile.ZipInfo(
                    filename=archive_name(relative_path, archive_root),
                    date_time=(1980, 1, 1, 0, 0, 0),
                )
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.flag_bits |= 0x800
                archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        os.replace(temporary_path, zip_path)
        zip_path.chmod(0o644)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

    external_checksum_path = zip_path.with_name(zip_path.name + ".sha256")
    external_checksum_path.write_text(
        f"{sha256_file(zip_path)}  {zip_path.name}\n",
        encoding="utf-8",
    )
    return external_checksum_path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate FILE_MANIFEST.csv and SHA256SUMS.txt. "
            "Optionally create a stable ZIP and an external checksum."
        )
    )
    parser.add_argument(
        "--zip",
        dest="zip_path",
        type=Path,
        help="Target path for the ZIP. Omit this option to create only release metadata.",
    )
    parser.add_argument(
        "--archive-root",
        default="",
        help="Optional visible top-level directory name inside the ZIP.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    matched_pairs, total_pairs, mismatched_models = statistical_release_gate()
    unexpected_mismatches = mismatched_models - {"Hybrid Poisson"}
    if unexpected_mismatches:
        raise SystemExit(
            "Release blocked: "
            "one or more models other than the documented Hybrid Poisson "
            "reconstruction no longer match the manuscript: "
            + ", ".join(sorted(unexpected_mismatches))
        )
    if matched_pairs != total_pairs:
        print(
            "Building version 2.0 with a disclosed Hybrid Poisson manuscript-"
            "concordance difference: "
            f"{matched_pairs} of {total_pairs} reported pairs match."
        )
    payload_files = collect_payload_files()
    rows = build_manifest_rows(payload_files)
    write_manifest(rows)
    write_checksums(payload_files)
    print(f"Wrote {MANIFEST_PATH}")
    print(f"Wrote {CHECKSUM_PATH}")

    if arguments.zip_path is not None:
        external_checksum = create_zip(arguments.zip_path, arguments.archive_root)
        print(f"Wrote {arguments.zip_path.expanduser().resolve()}")
        print(f"Wrote {external_checksum}")


if __name__ == "__main__":
    main()
