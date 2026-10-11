#!/usr/bin/env python3
"""Re-estimate the Hybrid Poisson model from the deposited analytic panel.

Run this script from either the package root or the code directory:

    python3 code/reproduce_hybrid_poisson.py

The implementation is the archived-panel reconstruction documented for
replication package version 2.0. It does not claim to recover the unavailable
original final model code.
"""

from __future__ import annotations

from reproduce_core_outputs import (
    HYBRID_FORMULA,
    TABLE_DIR,
    fit_hybrid_poisson,
    load_panel,
    prepare_main,
    write_hybrid_outputs,
)


def main() -> None:
    panel = load_panel()
    analysis_data = prepare_main(panel)
    hybrid_data, result = fit_hybrid_poisson(analysis_data)
    write_hybrid_outputs(hybrid_data, result)

    print("Hybrid Poisson re-estimation completed.")
    print(f"Formula: {HYBRID_FORMULA}")
    print(f"Observations: {int(result.nobs)}")
    print(f"Country clusters: {hybrid_data.loc[result.model.data.row_labels, 'iso3'].nunique()}")
    print(f"Results: {TABLE_DIR / 'table3_hybrid_poisson.csv'}")
    print(
        "Specification: "
        f"{TABLE_DIR / 'table3_hybrid_poisson_specification.csv'}"
    )


if __name__ == "__main__":
    main()
