#!/usr/bin/env python3
"""Remove only the 26 explicitly rejected v26 SVGs, with digest protection.

Run this script from the incoming checkpoint BEFORE merging that checkpoint
into a clean repository. Default is dry-run. No other path is ever deleted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

PREFIX = 'docs/physics/high-school/grade-11/assets/theory-figures/01-oscillations/'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True, help='Existing repository root')
    parser.add_argument('--apply', action='store_true', help='Delete verified retired files')
    args = parser.parse_args()
    root = args.root.resolve()
    if not (root / 'mkdocs.yml').is_file() or not (root / 'README.md').is_file():
        parser.error('Target does not look like an Education Hub source root.')
    ledger = json.loads(Path(__file__).with_name('ch1-theory-visual-ledger.json').read_text(encoding='utf-8'))
    pending: list[Path] = []
    for item in ledger['retired_assets']:
        rel = item['path']; pp = PurePosixPath(rel)
        if not rel.startswith(PREFIX) or pp.is_absolute() or '..' in pp.parts or pp.suffix != '.svg':
            parser.error(f'Unsafe retirement path: {rel}')
        candidate = root / rel
        if any(path.is_symlink() for path in [candidate, *candidate.parents] if path != root.parent):
            parser.error(f'Refusing symlink path: {rel}')
        if not candidate.exists():
            continue
        if not candidate.is_file() or hashlib.sha256(candidate.read_bytes()).hexdigest() != item['sha256']:
            parser.error(f'File changed since rejected v26; preserve it and resolve manually: {rel}')
        pending.append(candidate)
    # Validate ALL candidates before removing any of them.
    for candidate in pending:
        if args.apply:
            candidate.unlink()
    verb = 'Removed' if args.apply else 'Would remove'
    print(f'{verb} {len(pending)} verified, rejected Chapter I SVGs. Other assets are untouched.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
