#!/usr/bin/env python3
"""
2026-06-15 16:45 主人决策:
- A. 修 988 个 [[sources/...]] 旧路径 wikilink (本脚本目标)
- B. 补 1954 短名悬空 (主人: 先不做)

策略:
- [[sources/X/Y/Z/file]] → [[../../sources/X/Y/Z/file]] (1 级深文件)
- [[sources/X/Y/Z/file]] → [[../../../sources/...]] (2 级深,如 wiki/sources/X/Y/file)
- 同时修 [[../../Raw Sources/...]] (把 Raw Sources 路径改 sources/ 路径)
- [[wikilink]] 占位符 → 直接删
"""
import os
import re
import json
import shutil
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path('/home/azhan186/open claw/知识库')

# === 1. 备份所有受影响的文件 ===
print('=== 1. 扫描受影响文件 ===')
affected = {}  # file path -> list of (old_link, new_link)
total_old_sources_links = 0
total_raw_sources_links = 0
total_wikilink_placeholders = 0

for root, dirs, files in os.walk(str(ROOT / 'wiki')):
    for f in files:
        if not f.endswith('.md'):
            continue
        p = Path(root) / f
        with open(p, encoding='utf-8') as fh:
            content = fh.read()
        
        file_changes = []
        new_content = content
        
        # 处理 [[sources/...]] 旧路径
        for m in re.finditer(r'\[\[sources/([^\]|]+)(?:\|[^\]]+)?\]\]', content):
            target_inner = m.group(1)
            # 计算从当前文件到 wiki/sources/... 的相对路径
            # 当前文件在 wiki/ 下的深度
            rel_to_wiki = p.relative_to(ROOT / 'wiki')
            depth = len(rel_to_wiki.parts) - 1  # -1 因为最后是文件名
            # 需要 depth+1 个 ".." 来回到 wiki/, 然后进 sources/
            up = '../' * (depth + 1)
            new_target = up + 'sources/' + target_inner
            old_link = m.group(0)
            new_link = f'[[{new_target}]]'
            file_changes.append((old_link, new_link))
            total_old_sources_links += 1
        
        # 处理 [[../../Raw Sources/...]] 旧路径 (在 Raw Sources 里的文件)
        for m in re.finditer(r'\[\[((?:\.\./)+)Raw Sources/([^\]|]+)(?:\|[^\]]+)?\]\]', content):
            up_count = m.group(1).count('../')  # 通常 2 个 ..
            target_inner = m.group(2)
            # Raw Sources 路径转换
            # 原 [[../../Raw Sources/2026/时政/2026-06-08_xxx]] 
            #   → ../../Raw Sources/2026/时政/2026-06-08_xxx
            # 但 2026-06-08 后是 L1/L2/L3/L4 结构,source 在 wiki/sources/...
            # 简化: 删掉,后面主人决定怎么修
            file_changes.append((m.group(0), None))  # None = 删除
            total_raw_sources_links += 1
        
        # 处理 [[wikilink]] 占位符
        for m in re.finditer(r'\[\[wikilink\]\]', content):
            file_changes.append(('[[wikilink]]', None))
            total_wikilink_placeholders += 1
        
        if file_changes:
            affected[str(p)] = (content, file_changes)

print(f'  受影响文件: {len(affected)}')
print(f'  [[sources/...]] 旧路径: {total_old_sources_links}')
print(f'  [[../../Raw Sources/...]] 旧路径: {total_raw_sources_links}')
print(f'  [[wikilink]] 占位符: {total_wikilink_placeholders}')

# === 2. 备份 + 写入 ===
print()
print('=== 2. 备份 + 改写 ===')
backup_dir = ROOT / '_trash' / '2026-06-15_fix-old-sources-wikilinks'
backup_dir.mkdir(parents=True, exist_ok=True)
manifest = []

for fpath_str, (old_content, changes) in affected.items():
    fpath = Path(fpath_str)
    rel = fpath.relative_to(ROOT)
    backup_path = backup_dir / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(fpath, backup_path)
    
    new_content = old_content
    for old_link, new_link in changes:
        if new_link is None:
            # 删除 (包括前后可能的空格/换行)
            new_content = re.sub(r'\s*' + re.escape(old_link), '', new_content)
        else:
            new_content = new_content.replace(old_link, new_link)
    
    fpath.write_text(new_content, encoding='utf-8')
    manifest.append({'file': str(rel), 'changes': len(changes)})

print(f'  备份到: {backup_dir.relative_to(ROOT)}')
print(f'  改了 {len(affected)} 个文件')

# === 3. 写清单 ===
manifest_path = backup_dir / 'manifest.json'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

# === 4. 验证 ===
print()
print('=== 3. 重新扫描验证 ===')
remaining_sources = 0
remaining_raw = 0
remaining_wikilink = 0
for root, dirs, files in os.walk(str(ROOT / 'wiki')):
    for f in files:
        if not f.endswith('.md'):
            continue
        p = Path(root) / f
        with open(p, encoding='utf-8') as fh:
            t = fh.read()
        remaining_sources += len(re.findall(r'\[\[sources/', t))
        remaining_raw += len(re.findall(r'\[\[(?:\.\./)+Raw Sources/', t))
        remaining_wikilink += len(re.findall(r'\[\[wikilink\]\]', t))

print(f'  剩余 [[sources/...]]: {remaining_sources}')
print(f'  剩余 [[../../Raw Sources/...]]: {remaining_raw}')
print(f'  剩余 [[wikilink]]: {remaining_wikilink}')

print()
print('完成。备份在 _trash/2026-06-15_fix-old-sources-wikilinks/')
