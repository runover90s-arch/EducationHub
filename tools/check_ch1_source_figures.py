#!/usr/bin/env python3
"""Check Chapter I PDF crop provenance, assets and Markdown hooks (stdlib only).

This is an integrity check, not a replacement for reading the source PDF,
checking the physics, or running a full MkDocs/browser build.
"""
from __future__ import annotations

import hashlib
import json
import re
import struct
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'docs/physics/high-school/grade-11/assets/theory-figures/01-oscillations/'


def main() -> int:
    ledger = json.loads((ROOT / 'tools/ch1-theory-visual-ledger.json').read_text(encoding='utf-8'))
    errors: list[str] = []
    records = ledger['figures']
    ids: set[str] = set()
    paths: set[str] = set()
    hashes: set[str] = set()
    pages = {item['id']: item['pages'] for item in ledger['source_inventory']}
    for rec in records:
        fid, rel = rec['id'], rec['asset']
        pp = PurePosixPath(rel)
        if not rel.startswith(PREFIX) or pp.is_absolute() or '..' in pp.parts or pp.suffix != '.png':
            errors.append(f'{fid}: unsafe or unexpected asset path')
            continue
        if fid in ids or rel in paths or rec['output_sha256'] in hashes:
            errors.append(f'{fid}: duplicate ID, path or image content')
        ids.add(fid); paths.add(rel); hashes.add(rec['output_sha256'])
        asset = ROOT / rel
        if not asset.is_file() or asset.is_symlink():
            errors.append(f'{fid}: missing asset or symlink')
            continue
        data = asset.read_bytes()
        if not data.startswith(b'\x89PNG\r\n\x1a\n') or len(data) < 24:
            errors.append(f'{fid}: invalid PNG header')
            continue
        if list(struct.unpack('>II', data[16:24])) != rec['output_size_px']:
            errors.append(f'{fid}: PNG dimensions differ from ledger')
        if hashlib.sha256(data).hexdigest() != rec['output_sha256']:
            errors.append(f'{fid}: PNG digest differs from source-reviewed version')
        if not 1 <= rec['pdf_page_1_indexed'] <= pages[rec['source_id']]:
            errors.append(f'{fid}: PDF page out of range')
        if not re.fullmatch(r'[0-9a-f]{64}', rec['pdf_sha256']):
            errors.append(f'{fid}: source digest missing')
        lesson = ROOT / rec['lesson_file']
        if not lesson.is_file():
            errors.append(f'{fid}: missing lesson')
            continue
        text = lesson.read_text(encoding='utf-8')
        pattern = rf'<!-- ch1-source-figure: {re.escape(fid)} -->\n(.*?)<!-- /ch1-source-figure: {re.escape(fid)} -->'
        blocks = re.findall(pattern, text, re.S)
        if len(blocks) != 1:
            errors.append(f'{fid}: missing or duplicate Markdown block')
            continue
        block = blocks[0]
        images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)\{([^}]*)\}', block)
        if len(images) != 1:
            errors.append(f'{fid}: expected exactly one Markdown image')
            continue
        alt, target, attrs = images[0]
        if alt != rec['alt'] or len(alt.strip()) < 20 or 'loading=lazy' not in attrs:
            errors.append(f'{fid}: alt text/lazy loading differs or is missing')
        if (lesson.parent / target).resolve() != asset.resolve():
            errors.append(f'{fid}: image target does not match ledger')
        if rec['caption'] not in block or rec['explanation'] not in block:
            errors.append(f'{fid}: caption or explanation missing')
    for retired in ledger['retired_assets']:
        if (ROOT / retired['path']).exists():
            errors.append(f'retired generated image still present: {retired["path"]}')
    for path in (ROOT / PREFIX).iterdir():
        if path.is_file() and path.relative_to(ROOT).as_posix() not in paths:
            errors.append(f'unregistered teaching asset: {path.name}')
    if errors:
        for error in errors:
            print('ERROR:', error)
        return 1
    print(f'[ch1-source-figures] {len(records)} original PDF crops; source pages, PNG digests, links, alt text and captions: PASS.')
    print(f'[ch1-source-figures] {len(ledger["retired_assets"])} rejected generated SVGs absent. No source PDF required for this integrity check.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
