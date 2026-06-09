---
title: "NAS 升级 SOP：4×16T RAID 6"
type: project
tags: [NAS, RAID, 升级, 数据迁移, 知识库备份]
created: 2026-06-09
status: 等待硬盘采购
estimated_cost: ~4700 元
estimated_duration: 5-7 天
---

# 🦞 NAS 升级 SOP：4×16T RAID 6

> **目标**：把绿联 DXP4800 Plus 从「2×4T RAID 1（4T 可用）」升级到「4×16T RAID 6（32T 可用）」，不丢任何数据。
> 
> **状态**：⏳ 等待硬盘采购
> **创建日期**：2026-06-09
> **执行人**：主人 + 晨光

---

## ⚠️ 升级前必做：把本文件备份到 NAS 之外

**本文件存放在 NAS 上，升级期间 NAS 会关机/重建，本文件也会消失！**

升级前必须先把本文件备份到至少一个外部位置：

```bash
# 方法 A：飞书/微信文件传输（最快）
# 1. 打开本文件
cat /root/.openclaw/workspace/NAS升级SOP_4x16T_RAID6.md
# 2. 复制全文
# 3. 飞书「文件传输助手」发给自己

# 方法 B：scp 到本地电脑
# 在你的电脑终端执行：
scp root@NAS_IP:/root/.openclaw/workspace/NAS升级SOP_4x16T_RAID6.md ~/Desktop/

# 方法 C：直接复制 markdown 文件
# 把这个文件复制到电脑桌面或 USB 盘
```

**升级时你需要在另一台设备（电脑/手机）上查看本 SOP**——不要在 NAS 上查看。

---

## 📋 进度跟踪（完成打 ✅）

### 阶段 0：准备
- [ ] 下单 4 块希捷酷狼 Pro 16T
- [ ] 下单 1 个 USB 3.0 硬盘盒（3.5 寸带 12V 电源）
- [ ] 知识库云端备份（飞书/微信/GitHub）

### 阶段 1：硬盘到货验收
- [ ] 4 块硬盘全部到货
- [ ] 硬盘盒到货
- [ ] 4 块硬盘通电时间 < 100 小时
- [ ] 4 块硬盘 S.M.A.R.T. 健康状态 OK
- [ ] 4 块硬盘 badblocks 读写测试（可选，可后台跑）

### 阶段 2：物理更换
- [ ] 备份电影清单（M3U / 截图）
- [ ] 4T 盘 1 块留下做冷备份
- [ ] 4T 盘 1 块闲置/出二手
- [ ] NAS 关机 + 拔电源 + 拔网线
- [ ] 抽出 2 块 4T 盘
- [ ] 装入 4 块 16T 盘（盘位 1-2-3-4）
- [ ] 开机

### 阶段 3：组 RAID 6
- [ ] 进绿联管理界面
- [ ] 删除原 4T RAID 1 存储池
- [ ] 创建新存储池（RAID 6，Btrfs）
- [ ] 等待初始化完成（10-20 小时）

### 阶段 4：数据恢复
- [ ] 创建共享文件夹（Movies / Documents / KnowledgeBase）
- [ ] 知识库从云端恢复到 NAS
- [ ] 电影重新下载（按清单）

### 阶段 5：建立 3-2-1 备份
- [ ] 4T 冷备份盘装入硬盘盒
- [ ] 首次全量 rsync 到冷备份盘
- [ ] 验证冷备份盘可读
- [ ] 知识库 git push 到 GitHub 私有仓库
- [ ] 配 smartmontools 每周 S.M.A.R.T. 巡检
- [ ] 配硬盘告警推送到飞书/邮箱

---

## 🛒 采购清单

### 必备：硬盘（~4600 元）

| 物品 | 数量 | 推荐型号 | 单价 | 小计 | 备注 |
|------|------|---------|------|------|------|
| NAS 专用 HDD 16T | 4 | **希捷酷狼 Pro 16T**（ST16000NE000） | ~1150 | 4600 | 5年质保，300TB/年负载，企业级氦气封装 |

**备选硬盘**：
- 西数红盘 Pro 16T（WD161KFGX）—— ~1100-1300 元/块
- 西数金盘 16T（WD161KRYZ）—— 7×24 强化，~1500 元/块（贵但更稳）

**购买渠道**：
- 京东自营 / 天猫旗舰店
- 同一订单买 4 块（确保批次接近）
- **不要买第三方店铺**（翻新盘风险）
- 保留发票（保修用）

### 必备：硬盘盒（~100 元）

| 物品 | 数量 | 规格 | 单价 | 推荐品牌 |
|------|------|------|------|---------|
| USB 3.0 硬盘盒 | 1 | 3.5 寸 + 12V 电源适配器 | ~100 | 奥睿科 ORICO、优越者、绿联 |

**注意事项**：
- 必须支持 3.5 寸（4T 盘需要 12V 供电）
- USB 3.0 即可（机械盘速度上限 ~200 MB/s，USB 3.0 够用）
- 如果电脑有雷电口，可以买雷电盒（更贵但更快，机械盘意义不大）

### 可选：升级配件
- 防静电手环（~20 元）—— 换硬盘时保护主板
- 硬盘防震垫（4 块 ~30 元）—— NAS 内减少振动噪音
- 标签贴纸（~10 元）—— 给硬盘贴编号 1-2-3-4

---

## 📦 阶段 0 详细操作：知识库云端备份

**重要**：升级 NAS 前，必须先把 83MB 知识库备份到 NAS 之外的地方。

### 方法 A：飞书/微信文件传输（最快）⭐

```bash
# 1. 打包知识库
cd /home/azhan186
tar -czf knowledge_backup_20260609.tar.gz "open claw/知识库/"

# 2. 检查大小
ls -lh knowledge_backup_20260609.tar.gz
# 预期：~80MB

# 3. 通过飞书「文件传输助手」发给自己
#    或者微信「文件传输」发给自己
```

### 方法 B：GitHub 私有仓库（最优雅）

```bash
# 1. 在 GitHub 创建私有仓库：knowledge-base-backup
#    https://github.com/new
#    仓库名：knowledge-base-backup
#    可见性：Private
#    不要勾选 README（避免冲突）

# 2. 添加 remote 并推送
cd "/home/azhan186/open claw/知识库"
git remote add backup https://github.com/你的用户名/knowledge-base-backup.git
git push -u backup main
# 第一次推送 83MB，5 秒完成

# 3. 之后每次改动只需
git push backup main
```

### 方法 C：百度网盘 / OneDrive / 阿里云盘

```bash
cd /home/azhan186
tar -czf knowledge_backup_20260609.tar.gz "open claw/知识库/"
# 然后用网盘客户端上传 ~80MB 文件
```

**建议做两个以上备份**（双保险）：
- 飞书文件传输助手 ✓
- GitHub 私有仓库 ✓

---

## 📦 阶段 1 详细操作：硬盘验收

### 1.1 S.M.A.R.T. 健康度检查

```bash
# 装上 smartmontools
sudo apt install smartmontools   # Linux
# 或 brew install smartmontools   # macOS

# 假设新硬盘在 /dev/sdb
sudo smartctl -a /dev/sdb

# 重点看：
# - Reallocated_Sector_Count：应为 0
# - Current_Pending_Sector：应为 0
# - Offline_Uncorrectable：应为 0
# - Power_On_Hours：应 < 100 小时（新盘）
# - UDMA_CRC_Error_Count：应为 0
```

### 1.2 全盘读写测试（可选，但建议做）

```bash
# 写读测试，约 8-10 小时
sudo badblocks -wsv /dev/sdb

# -w 写测试
# -s 显示进度
# -v 显示坏块详情
# 测试完成后没坏块就 OK
```

### 1.3 序列号记录

每块硬盘拍序列号标签照片，存到知识库：
- 硬盘 1 序列号：`Z________________`
- 硬盘 2 序列号：`Z________________`
- 硬盘 3 序列号：`Z________________`
- 硬盘 4 序列号：`Z________________`

**保修需要序列号！**

---

## 📦 阶段 2 详细操作：物理更换

### 2.1 备份电影清单（可选）

如果你用 Jellyfin / Plex / Emby / 群晖 Video Station 管理电影：

```bash
# 导出 M3U 播放列表
# 在媒体服务器管理界面 → 导出 → 保存到本地

# 或者截图记录文件夹结构
# 树状图命令：
tree /volume1/Movies -L 3 > /tmp/movies_listing.txt
```

### 2.2 关机操作

```
⚠️ 严格按顺序：
1. 进绿联管理界面 → 关机
2. 等待 1 分钟（让硬盘磁头归位）
3. 拔掉电源线
4. 拔掉网线（防止误启动）
5. 等 30 秒（电容放电）
```

### 2.3 换盘操作

```
1. 打开 NAS 前盖（一般是免螺丝卡扣设计）
2. 抽出 2 块 4T 硬盘（注意编号位置）
3. 4 块 16T 装入盘位 1-2-3-4
4. 确保硬盘完全插入到位
5. 装回前盖
6. 插电源、插网线
7. 按开机键
```

### 2.4 旧盘处理

- **4T 盘 #1**：装入新买的 USB 硬盘盒，做冷备份盘
- **4T 盘 #2**：闲置备用 / 闲鱼出二手（~150-200 元）

---

## 📦 阶段 3 详细操作：组 RAID 6

### 3.1 进绿联管理界面

浏览器访问：
- `http://NAS的IP:9999`（如果记得 IP）
- 或者 `http://find.ugnas.com`（绿联自动发现）

### 3.2 删除旧存储池

```
存储管理 → 存储池 → 找到原 4T RAID 1 → 删除
系统会二次确认，**确认数据已备份**后再删
```

### 3.3 创建新存储池

```
存储管理 → 存储池 → 创建

存储池名称：MainPool
RAID 类型：**RAID 6**（双盘容错）
文件系统：Btrfs（绿联默认）
硬盘选择：勾选全部 4 块 16T

点击创建 → 等待 10-20 小时完成初始化
期间：
- ✅ 可以进管理界面做其他配置
- ❌ 不要存重要数据
- ❌ 不要断电
```

### 3.4 创建存储空间

```
存储空间 → 创建
路径：/volume1
文件系统：Btrfs
```

### 3.5 创建共享文件夹

```
控制面板 → 共享文件夹 → 创建

/volume1/Movies           - 电影
/volume1/Documents        - 资料
/volume1/KnowledgeBase    - 知识库

权限设置：
- 主人：读写
- 其他人：按需
```

---

## 📦 阶段 4 详细操作：数据恢复

### 4.1 知识库恢复

```bash
# 方法 A：从 tar 包恢复
cd /home/azhan186
tar -xzf knowledge_backup_20260609.tar.gz
# 恢复到原位置

# 方法 B：从 GitHub 克隆
cd /home/azhan186/open\ claw
git clone https://github.com/你的用户名/knowledge-base-backup.git 知识库_new
# 核对内容后，删除旧知识库，重命名 _new 为 知识库
```

### 4.2 验证知识库

```bash
# 检查文件数
find "/home/azhan186/open claw/知识库" -type f | wc -l
# 预期：~1500+ 个文件（357 wiki + 大量 Raw Sources）

# 检查 Raw Sources 数量
ls "/home/azhan186/open claw/知识库/图书馆/Raw Sources/"*/ 2>/dev/null | wc -l
```

### 4.3 电影重新下载

按你的清单：
- PT 站优先（速度快、资源好）
- 115 网盘 / 阿里云盘
- BT 辅以

下载到 `/volume1/Movies/`

---

## 📦 阶段 5 详细操作：建立 3-2-1 备份

### 5.1 4T 冷备份盘配置

```bash
# 1. 4T 盘装入 USB 硬盘盒
# 2. 插到 NAS（或者直接插电脑）
# 3. 格式化为 ext4（Linux）或 exFAT（跨平台）
sudo mkfs.ext4 /dev/sdc1

# 4. 挂载
sudo mkdir -p /mnt/coldbackup
sudo mount /dev/sdc1 /mnt/coldbackup

# 5. 首次全量备份
rsync -av --delete "/home/azhan186/open claw/知识库/" /mnt/coldbackup/knowledge/
rsync -av --delete "/volume1/Documents/" /mnt/coldbackup/documents/
```

### 5.2 冷备份盘原则

⚠️ **冷备份盘平时不挂在 NAS 上**：
- 防勒索软件（自动加密挂载的网络盘）
- 防意外删除扩散
- 防 NAS 系统故障
- **只在每次备份时插上，备份完拔掉**

### 5.3 配 S.M.A.R.T. 监控

```bash
# 安装 smartmontools（NAS 上）
sudo apt install smartmontools

# 每周日凌晨 3 点巡检
crontab -e
# 添加：
0 3 * * 0 /usr/sbin/smartctl -a /dev/sda > /var/log/smart_weekly_$(date +\%Y\%m\%d).log
0 3 * * 0 /usr/sbin/smartctl -a /dev/sdb >> /var/log/smart_weekly_$(date +\%Y\%m\%d).log
0 3 * * 0 /usr/sbin/smartctl -a /dev/sdc >> /var/log/smart_weekly_$(date +\%Y\%m\%d).log
0 3 * * 0 /usr/sbin/smartctl -a /dev/sdd >> /var/log/smart_weekly_$(date +\%Y\%m\%d).log
```

### 5.4 配硬盘告警

绿联管理界面：
```
系统设置 → 通知 → 硬盘 S.M.A.R.T. 告警
- 启用邮件通知：填主人邮箱
- 启用飞书通知：填飞书 Webhook
```

---

## ❓ 常见问题

### Q1: 升级期间 NAS 上的 OpenClaw 还能用吗？
**A**: 不能。物理换盘 + RAID 重建期间，NAS 完全离线。

### Q2: 知识库在升级期间还能访问吗？
**A**: 不能。NAS 关机后，OpenClaw 也会停止运行。
**所以一定要先备份！** 我们做的飞书/GitHub 备份就是为了应对这个。

### Q3: 升级失败回退方案？
**A**: 如果 RAID 6 初始化失败：
- 4 块 16T 盘应该都还是好的
- 重新尝试初始化
- 如果反复失败，联系绿联客服 / 希捷客服
- 旧 4T RAID 1 数据已经在云端备份的电影清单 + 知识库 + 4T 冷备份盘上都有

### Q4: 32T 不够用怎么办？
**A**: 32T 实际约 28-29 TiB。够用的话：
- 2026-2028 年：绰绰有余（电影 2-3T + 资料 1T + 余量 24T）
- 2029 年以后：可以再加一台 NAS / 改用更大硬盘重建 RAID

### Q5: 噪音大吗？
**A**: 4 块 16T 盘同时运行会比 2 块 4T 稍响：
- NAS 放客厅：建议远离床头
- NAS 放书房/杂物间：基本无感
- 希捷酷狼 Pro 噪音控制：~28 dB（待机）/ ~32 dB（读写）

### Q6: 电费会增加吗？
**A**: 4 块 16T vs 2 块 4T：
- 单盘功耗差不多（~7-8W）
- 多 2 块盘约 +15W
- 每天多 0.36 度电，每年多 ~130 度电
- 上海阶梯电价，每年多约 ~80 元

---

## 🔗 相关知识

- 知识库 wiki：[[RAID-Levels-Comparison]]（待创建）
- 知识库 wiki：[[3-2-1-Backup-Strategy]]（待创建）
- 知识库 wiki：[[NAS-Hardware-Maintenance]]（待创建）

---

## 📞 执行时联系我

任何阶段遇到问题，随时找我：
- 飞书直接发消息
- 或说"继续升级"

我会陪你一步步走完整个流程。

---

*文件创建于 2026-06-09*
*最后更新：2026-06-09*
*等待硬盘采购完成*
