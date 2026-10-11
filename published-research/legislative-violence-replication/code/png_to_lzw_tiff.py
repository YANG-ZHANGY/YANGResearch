"""Convert a 600 dpi PNG to a lossless LZW-compressed TIFF."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: png_to_lzw_tiff.py INPUT.png OUTPUT.tiff")
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    with Image.open(source) as image:
        rgba = image.convert("RGBA")
    rgba.save(source, format="PNG", dpi=(600, 600), compress_level=6)
    rgba.convert("RGB").save(
        destination,
        format="TIFF",
        compression="tiff_lzw",
        dpi=(600, 600),
    )


if __name__ == "__main__":
    main()
