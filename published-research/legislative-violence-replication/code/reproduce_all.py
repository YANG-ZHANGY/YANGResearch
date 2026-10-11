#!/usr/bin/env python3
"""Run the complete statistical and publication-figure workflow."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CODE_DIR = PACKAGE_ROOT / "code"


def run(command: list[str]) -> None:
    print("+", " ".join(command), flush=True)
    completed = subprocess.run(command, cwd=PACKAGE_ROOT, check=False)
    if completed.returncode != 0:
        raise SystemExit(
            f"Workflow stopped: {Path(command[-1]).name} returned "
            f"status {completed.returncode}."
        )


def main() -> None:
    rscript = shutil.which("Rscript")
    if rscript is None:
        raise SystemExit("Rscript is required to render the publication figures.")
    run([sys.executable, str(CODE_DIR / "reproduce_core_outputs.py")])
    run([sys.executable, str(CODE_DIR / "generate_codebook.py")])
    run([rscript, str(CODE_DIR / "render_publication_figures.R")])
    run([sys.executable, str(CODE_DIR / "validate_reproduction.py")])
    print("Complete reproduction finished successfully.")


if __name__ == "__main__":
    main()
