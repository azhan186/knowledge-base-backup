---
title: "WebDAV 协议说明"
type: source
tags: [WebDAV, HTTP, 远程文件管理, NAS, Nextcloud, Synology, 协作]
sources: [../../图书馆/Raw Sources/技术参考/其他技术/2026-05-21_WebDAV协议说明.md]
last_updated: 2026-06-11
date: 2026-05-21
---

# WebDAV 协议说明

> 视角：基于 HTTP 的扩展协议——让远程文件管理像操作本地一样。

## 概述

**WebDAV**（Web-based Distributed Authoring and Versioning）= 基于 HTTP 协议的扩展，用于**网络上远程文件管理与协作**。

## 核心特点与功能

### 文件操作支持

通过 WebDAV 客户端，对远程服务器进行**创建、读取、更新、删除、重命名、移动、复制**等操作，类似本地文件系统。

### 目录管理

- 创建、删除、检索目录
- 便于组织文件结构

### 锁定机制

- **独占锁**：防止多用户同时编辑
- **共享锁**：允许只读并发，写入互斥
- 防止数据冲突，确保一致性

### 元数据管理

- 用户定义和操作文件元数据（标题、作者、自定义标签）
- 以 XML 格式存储和交换

## 工作原理

WebDAV 在 HTTP 协议基础上扩展以下方法：

| HTTP 方法 | 用途 |
|----------|------|
| PROPFIND | 获取属性 |
| PROPPATCH | 修改属性 |
| MKCOL | 创建目录 |
| COPY | 复制资源 |
| MOVE | 移动资源 |
| LOCK / UNLOCK | 加锁/解锁 |
| REPORT | 高级查询 |

## 应用场景

| 场景 | 典型实现 |
|------|---------|
| **个人云盘** | Nextcloud、ownCloud |
| **NAS 自托管** | Synology、QNAP、Unraid |
| **团队协作** | SharePoint、Alfresco |
| **笔记同步** | Obsidian + Remotely Save |
| **代码协作** | 部分 Git forges |

## vs 其他协议

| 协议 | 优势 | 劣势 |
|------|------|------|
| **WebDAV** | 标准 HTTP 扩展，防火墙友好 | 大文件分块效率一般 |
| **SFTP** | 加密稳定 | 不是 HTTP，浏览器不友好 |
| **S3** | 云原生，分片上传 | 私有化部署复杂 |
| **SMB/CIFS** | Windows 友好 | 跨平台一般 |

## 相关概念

- [[Remotely_Save插件说明]]
- [[知识库规范]]

---

*编译：2026-06-11*