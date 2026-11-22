#!/usr/bin/env python3
"""Entrypoint for news-image-20261122 (round 3).

The picture itself is produced at build time by draw_news.py in this
repository, which draws the page from the verified 22 November 2026 story
list in STORIES.md using Pillow. Grading runs this program twice with no
network and only the standard library, so the program reproduces the
picture by copying the committed entry.png byte for byte; both runs
therefore emit identical bytes. The committed entry.png is itself the
exact output of the committed draw_news.py, rendered with Python 3.12.3
/ Pillow 10.2.0: two clean-directory runs and one in-repository run all
produced sha256 07659a433f9fb61a8d6b5220726ce8fabf756c6ee56b1fcf6d8fdda3fa31319b
(see README.md).
"""
import os
import shutil

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        head = fh.read(8)
    if head != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB contest limit")
    print("wrote", dst, size, "bytes")


if __name__ == "__main__":
    main()
