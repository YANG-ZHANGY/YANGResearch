# Software Environment

## Tested environment

- Operating system: macOS on arm64, Darwin 24.6.0
- Python: 3.9.6
- pandas: 2.2.3
- NumPy: 2.0.2
- statsmodels: 0.14.6
- Pillow: 11.3.0
- SciPy: 1.13.1
- R: 4.6.1
- ggplot2: 4.0.3
- scales: 1.4.0
- jsonlite: 2.0.0
- Poppler `pdfinfo`: 26.05.0

Exact replication does not require the same operating system, but output fonts and PDF rendering can vary slightly across platforms.

## Complete workflow

From the package root:

```bash
python3 code/reproduce_all.py
```

The workflow recreates the statistical tables, panel summaries, model-fit summaries, coefficient comparisons, codebook, publication figures, and model-derived figure data. It then validates all reported values and publication-file specifications.

This workflow starts from the archived analytic panel. It does not reconstruct that panel from the upstream datasets.

The validation step returns success after checking the panel, successful convergence of all seven models, the dedicated Hybrid Poisson outputs, figure source files, publication-file specifications, and the codebook. It separately reports that 36 of 41 displayed manuscript coefficient-and-standard-error pairs match and that the five differences are confined to the documented Hybrid Poisson reconstruction. `documentation/REPRODUCTION_VALIDATION.md` records the comparison.

## Core statistical workflow

To recreate only the statistical outputs:

```bash
python3 code/reproduce_core_outputs.py
```

## Hybrid Poisson workflow

To re-estimate only the Hybrid Poisson reconstruction from the deposited panel:

```bash
python3 code/reproduce_hybrid_poisson.py
```

This command writes `tables/table3_hybrid_poisson.csv` and `tables/table3_hybrid_poisson_specification.csv`. The model construction, formula, analysis sample, covariance estimator, and interpretation boundary are documented in `documentation/HYBRID_POISSON_SPECIFICATION.md`.

## Codebook workflow

From the package root:

```bash
python3 code/generate_codebook.py
```

The script reads the analytic panel and recreates `documentation/codebook.csv`, with one row for each of the panel's 86 fields.

## Publication-figure workflow

From the package root:

```bash
Rscript code/render_publication_figures.R
```

The R script uses ggplot2, scales, and jsonlite. It reads the machine-readable files in `source_data/`, generates the three figures, and writes single-page PDF and 600 dpi PNG files to `figures/`. It then calls:

```bash
python3 code/png_to_lzw_tiff.py INPUT.png OUTPUT.tiff
```

The helper uses Pillow to create 600 dpi RGB TIFF files with lossless LZW compression.

## Figure-source scope

- Figure 1 is drawn from country incident counts and the deposited Natural Earth GeoJSON.
- Figure 2 is drawn from `figure2_publication_source.csv`, which reproduces the manuscript curves and interval envelopes. The original plotting dataset was not retained in the archived materials.
- Figure 3 is drawn from the deposited leave-one-country-out coefficient file.
- `figure2_model_recomputed_check.csv` contains predictions recomputed by the core Python workflow and is separate from the publication curve file.
- `figure3_model_recomputed_check.csv` contains leave-one-country-out estimates independently recomputed by the core Python workflow and is separate from the publication figure source.

## Output specifications

- Figure 1 PNG: 4,251 × 3,590 pixels
- Figure 2 PNG: 4,251 × 2,929 pixels
- Figure 3 PNG: 4,251 × 5,622 pixels
- PNG resolution: 600 dpi
- TIFF resolution: 600 dpi
- TIFF compression: LZW
- PDF: one page per file, white background, embedded vector drawing where supported

## Archive-building workflow

After the complete workflow and validation succeed, run:

```bash
python3 code/build_release_artifacts.py \
  --zip ../Harvard_Dataverse_Replication_v2.0.zip \
  --archive-root Harvard_Dataverse_Replication_v2.0
```

The script checks that manuscript-concordance differences are confined to the documented Hybrid Poisson reconstruction, creates `FILE_MANIFEST.csv` and `SHA256SUMS.txt` in the package root, then creates the requested ZIP and a neighboring `.zip.sha256` file. ZIP members are sorted and assigned stable timestamps and permissions to support byte-for-byte recreation when the package content is unchanged.
