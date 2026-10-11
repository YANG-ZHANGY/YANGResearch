# Hybrid Poisson Reproduction Specification

## Scope

Version 2.0 includes a fully executable within-between Hybrid Poisson reconstruction based on the deposited analytic panel. The original code that generated the manuscript's final Hybrid Poisson estimates was not retained. This implementation therefore reproduces the documented model logic from the available variables and does not claim byte-for-byte or estimate-for-estimate identity with the unavailable original code.

## Run command

From the package root:

```bash
python3 code/reproduce_hybrid_poisson.py
```

The same model is also included in the complete workflow:

```bash
python3 code/reproduce_all.py
```

## Input and analysis sample

- Input: `data/merged_europe_panel.csv`
- Unit of analysis: country-year
- Outcome: `count`, the recorded number of legislative-violence incidents
- Country identifier and clustering variable: `iso3`
- Complete-case variables: `count`, `countb`, `pi_z`, `closure`, `pol`, `log10_gdp`, `enpp`, `lsq`, `iso3`, `country`, and `year`
- Time controls: five-year period indicators beginning with 1980–1984

The script records the realized observation and country-cluster counts in `tables/table3_hybrid_poisson_specification.csv`.

## Variable construction

For country \(i\) and year \(t\), all country means are calculated after the
complete-case analysis sample has been formed:

- `pi_between` is the country mean of `pi_z`.
- `pi_within` is `pi_z` minus its country mean.
- `closure_between` is the country mean of `closure`. It is retained as a
  decomposition record but is not included as a regressor in the specified
  formula.
- `closure_within` is `closure` minus its country mean.
- `closure_within_sq` is the square of `closure_within`.
- `pol_c` is `pol` centred on the complete analysis sample mean.

## Estimator

The model is a Poisson generalized linear model with a log link:

```text
count ~ pi_between + pi_within + closure_within + closure_within_sq
      + closure_within:pol_c + log10_gdp + enpp + lsq + C(year_bin)
```

The covariance matrix uses cluster-robust standard errors grouped by `iso3`.

## Outputs

- `tables/table3_hybrid_poisson.csv`: coefficients, cluster-robust standard errors, p values, z values, 95% confidence intervals, formatted estimates, and analysis-sample size.
- `tables/table3_hybrid_poisson_specification.csv`: formula, estimator family, covariance type, clustering variable, observation count, country-cluster count, and time grouping.
- `tables/table3_extended_models.csv` and `tables/table3_extended_models_tidy.csv`: the Hybrid Poisson estimates alongside the other Table 3 robustness models.
- `tables/manuscript_reported_vs_reproduced_coefficients.csv`: side-by-side manuscript and version 2.0 estimates.

## Interpretation boundary

Successful execution demonstrates that the deposited data and version 2.0 code are sufficient to estimate this specified Hybrid Poisson model. The generated Hybrid Poisson values differ from the manuscript's five displayed estimates. That manuscript-concordance difference is retained in `documentation/REPRODUCTION_VALIDATION.md` rather than concealed or treated as an execution failure.
