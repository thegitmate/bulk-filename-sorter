#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# v1 by thegitmate (n)

from __future__ import annotations

import os
import shutil
from pathlib import Path


def pick_target_folder(base: Path, user_input: str) -> Path:
    """
    Resolve user input to a folder:
    - If user_input is an absolute/relative path, use it.
    - Otherwise, look for a direct child folder of `base` matching the name (case-sensitive then case-insensitive).
    """
    s = user_input.strip().strip('"').strip("'")
    if not s:
        raise ValueError("Empty file name.")

    p = Path(s).expanduser()
    if not p.is_absolute():
        p = (base / p).resolve()

    if p.exists() and p.is_dir():
        return p

    # Fallback: look for a child folder with that exact name (then case-insensitive)
    direct = base / s
    if direct.exists() and direct.is_dir():
        return direct.resolve()

    low = s.casefold()
    for child in base.iterdir():
        if child.is_dir() and child.name.casefold() == low:
            return child.resolve()

    raise FileNotFoundError(
        f"Unable to find the file: '{user_input}'.\n"
        f"Tip: you can enter the file name or the path (ex: ./Holiday Images)."
    )


def safe_destination_folder(root: Path, keyword: str) -> Path:
    """
    Create a destination folder under root named keyword.
    If it exists, create keyword_2, keyword_3, ...
    """
    base_name = keyword.strip()
    if not base_name:
        raise ValueError("Mot-clé vide.")

    dest = root / base_name
    if not dest.exists():
        dest.mkdir(parents=True)
        return dest

    i = 2
    while True:
        candidate = root / f"{base_name}_{i}"
        if not candidate.exists():
            candidate.mkdir(parents=True)
            return candidate
        i += 1


def unique_move(src: Path, dest_dir: Path) -> Path:
    """
    Move src into dest_dir. If a file with same name exists, append (1), (2), ...
    """
    dest = dest_dir / src.name
    if not dest.exists():
        shutil.move(str(src), str(dest))
        return dest

    stem, suffix = src.stem, src.suffix
    i = 1
    while True:
        dest = dest_dir / f"{stem} ({i}){suffix}"
        if not dest.exists():
            shutil.move(str(src), str(dest))
            return dest
        i += 1


def main() -> None:
    base = Path.cwd()

    folder_input = input(
        f"[base path: {base}]\n\nFolder to scan (name or path):\n> "
    )
    target = pick_target_folder(base, folder_input)

    keyword = input("Keyword to search in the files' NAME:\n> ").strip().strip('"').strip("'")
    if not keyword:
        print("Empty keyword, stopped.")
        return

    # Destination folder created inside the target folder (so everything stays together)
    dest_dir = safe_destination_folder(target, keyword)

    key = keyword.casefold()
    moved = 0
    skipped = 0

    # Walk recursively
    for root, dirs, files in os.walk(target):
        root_path = Path(root)

        # Do not walk into the destination folder we create
        # (and avoid moving files already in it)
        if root_path == dest_dir:
            continue
        if dest_dir.name in dirs:
            dirs.remove(dest_dir.name)

        for name in files:
            if key in name.casefold():
                src = root_path / name

                # Don’t move the script itself if it matches
                try:
                    if src.resolve() == Path(__file__).resolve():
                        skipped += 1
                        continue
                except Exception:
                    pass

                unique_move(src, dest_dir)
                moved += 1

    print(f"\n✅ Done.")
    print(f"📁 File scanned : {target}")
    print(f"🎯 Keyword       : {keyword}")
    print(f"📦 Destination   : {dest_dir}")
    print(f"➡️  Filed moved : {moved}")
    if skipped:
        print(f"⏭️  Skipped : {skipped}")


if __name__ == "__main__":
    main()
