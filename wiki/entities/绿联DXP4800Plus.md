---
title: "绿联 DXP4800 Plus"
type: entity
tags: [NAS, 绿联, 设备]
sources: []
last_updated: 2026-05-12
---

# 绿联 DXP4800 Plus NAS

## 基本信息
- **品牌**：绿联（UGREEN）
- **型号**：DXP4800 Plus
- **系统**：Debian GNU/Linux 12 (bookworm)
- **类型**：四盘位 NAS

## 硬件配置
- **CPU**：Intel Pentium Gold 8505
- **内存**：15GB
- **存储**：3.6TB（已使用 1%）

## 系统限制
- apt 源受限，无法安装 cron
- 需要替代方案实现定时任务

## 替代定时方案
1. OpenClaw Heartbeat 机制
2. 后台脚本循环
3. 外部定时服务（如 IFTTT、Webhook）

---
*更新时间：2026-05-12*
## 关联页面

- [NAS存储概念.md](NAS存储概念.md)
