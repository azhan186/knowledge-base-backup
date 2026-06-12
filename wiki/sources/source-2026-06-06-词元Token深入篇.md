---
title: "词元Token深入篇"
type: source
subject: "520 计算机科学"
tags: [图书馆, AI与科技, 词元Token, BPE, WordPiece, 深入篇, 2026-06-06]
sources:
  - "../../图书馆/Raw Sources/AI与科技/2026-06-06_词元Token深入篇.md"
last_updated: 2026-06-10
date: 2026-06-06
---

# 词元Token深入篇

> 视角：分词算法与编码

## 三大主流分词算法

### 1. BPE（Byte Pair Encoding）
- **GPT 系列**采用
- 从字符开始，**迭代合并高频对**
- 平衡词表大小与表达力

### 2. WordPiece
- **BERT**采用
- 类似 BPE，但用**似然度**选择合并对
- 偏向保留**有意义的子词**

### 3. SentencePiece / Unigram
- 语言无关
- 直接从句子学习
- 日语/中文/多语言常用

## 关键数字

| 模型 | 词表大小 |
|------|----------|
| GPT-2 | 50,257 |
| GPT-4 | ~100,000 |
| LLaMA | 32,000 |
| 中文模型 | 60,000+ |

## 工程含义

- **API 成本** = token 数 × 单价
- **上下文窗口** = token 上限
- **多语言效率**：中文 token 化效率比英文低

## 关联

- [[词元Token]] — 主卡
- [[词元Token资深篇]] — 下一档
