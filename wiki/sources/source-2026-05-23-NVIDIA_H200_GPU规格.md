---
title: "NVIDIA H200 GPU 规格与架构"
type: source
tags: [NVIDIA, H200, Hopper, HBM3e, AI训练, 推理, GPU, AI硬件]
sources: ["Raw Sources/技术参考/2026-05-23_NVIDIA_H200_GPU规格.md"]
last_updated: 2026-05-23
---

# NVIDIA H200 GPU 规格与架构

## 核心规格

| 规格项 | 参数 |
|--------|------|
| 架构 | NVIDIA Hopper（台积电 4nm） |
| 显存 | 141GB HBM3e（vs H100 80GB，+76.25%） |
| 带宽 | 4.8 TB/s（vs H100 3.35 TB/s，+43.28%） |
| FP8 算力 | ~1,979 TFLOPS |
| TDP | 700W（SXM） |

## 架构定位

H200 = H100 内存增强版，核心与 H100 一致，强项在于减少数据等待：
- 推理速度可达 H100 的 **1.9 倍**
- GPT-3 训练性能提升 **60%-90%**
- 内存密集型 HPC 比 x86 CPU **快 110 倍**

## 竞品定位

| 竞品 | H200 优势 |
|------|-----------|
| H100 | 显存+76%，带宽+43% |
| H20（对华特供） | FP8 算力是 H20 的 **6.7 倍** |
| Intel Gaudi 3 | Llama 3.1 405B 推理速度快 **9 倍** |
| AMD MI300X | 多项领先 |

## 相关链接

- [[Nas存储概念]] — NAS 与 GPU 计算的关系（可用于本地 AI 推理）
- 算力与本地设备选型相关