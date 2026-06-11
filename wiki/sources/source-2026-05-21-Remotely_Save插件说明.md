---
title: "Remotely Save 插件说明"
type: source
tags: [Obsidian, Remotely Save, 同步插件, S3, WebDAV, 多设备同步]
sources: [../../图书馆/Raw Sources/技术参考/其他技术/2026-05-21_Remotely_Save插件说明.md]
last_updated: 2026-06-11
date: 2026-05-21
---

# Remotely Save 插件说明

> 视角：Obsidian 第三方同步插件——把本地笔记库与远程云存储同步，实现多设备实时备份。

## 核心特点

### 支持多种云存储服务

- S3（Amazon S3、Cloudflare R2、Backblaze B2）
- Dropbox
- WebDAV（Nextcloud、Synology）
- OneDrive（个人版）
- Google Drive

### 灵活同步配置

- 同步频率：每 5 分钟 / 每 30 分钟 / 手动触发
- **增量同步**：仅传输变更文件，效率高
- 选择性同步：可排除指定目录

### 冲突处理机制

- **保留最新版本**（默认）
- **备份冲突文件**（推荐开启，避免数据丢失）
- 手动合并选项

### 跨平台兼容

- Windows、macOS、Linux、iOS、Android 全平台
- 确保不同设备上 Obsidian 笔记数据一致

## 使用场景

| 场景 | 推荐配置 |
|------|---------|
| **个人多设备** | Dropbox + 每 5 分钟同步 + 备份冲突 |
| **NAS 自托管** | WebDAV (Synology) + 手动同步 + 保留最新 |
| **云端备份** | S3 (Cloudflare R2) + 每 30 分钟 + 完整加密 |
| **团队协作** | WebDAV (Nextcloud) + 锁定机制 |

## 性能优化

- **排除不必要的目录**：如 `.trash/`、`.obsidian/workspace.json`
- **批量同步**：避免每次单文件同步
- **压缩传输**：开启 gzip 减少带宽

## 相关概念

- [[WebDAV协议说明]]
- [[知识库规范]]（本知识库使用 Obsidian + Remotely Save + NAS 备份）

---

*编译：2026-06-11*