# Remotely Save 插件说明

> 原始信息 | 来源：网络资料整理 | 时间：2026-05-21

---

## 概述

Remotely Save 是一款用于 Obsidian 笔记软件的第三方同步插件，主要功能是将本地 Obsidian 笔记库与远程云存储服务进行同步，实现多设备间笔记数据的实时或定期同步。

---

## 核心特点

### 支持多种云存储服务
支持 S3（Amazon S3、Cloudflare R2、Backblaze B2 等）、Dropbox、WebDAV（Nextcloud、Synology 等）、OneDrive（个人版）、Google Drive 等主流云存储平台，用户可根据需求选择适合的存储服务。

### 灵活同步配置
可设置同步频率（如每5分钟、每30分钟自动同步，或手动触发同步），支持增量同步，仅传输变更的文件，提高效率。

### 冲突处理机制
当多设备同时修改同一文件时，提供冲突检测与处理策略，如保留最新版本、备份冲突文件等，避免数据丢失。

### 跨平台兼容
可在 Windows、macOS、Linux、iOS、Android 等系统上的 Obsidian 中安装使用，确保不同设备间笔记数据的一致性。

---

## 使用场景

适用于需要在多台设备（电脑、手机、平板）上查看、编辑 Obsidian 笔记，并希望笔记数据能自动同步到云端备份或共享的用户，尤其适合对 Obsidian 官方同步服务费用敏感或希望使用自定义云存储方案的用户。

---

## 关键词
Remotely Save、Obsidian、插件、同步、S3、WebDAV、Dropbox、OneDrive、Google Drive、增量同步、冲突处理、跨平台