# ComfyUI + FLUX 安装指南（Windows + RTX 5070）

## 前提
- Windows 10/11
- NVIDIA RTX 5070（推荐16GB+显存）
- 100GB+ 硬盘空间

---

## 一、安装步骤

### 1. 安装 Python（推荐使用 pyenv-win）
```bash
# 或者直接下载 Python 3.11/3.10
# https://www.python.org/downloads/
# 安装时勾选 "Add Python to PATH"
```

### 2. 克隆 ComfyUI
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
```

### 3. 创建虚拟环境并安装依赖
```bash
python -m venv venv
venv\Scripts\activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

### 4. 下载 FLUX 模型权重
```
从 https://huggingface.co/black-forest-labs/FLUX.1-dev 下载：
- flux1-dev.safetensors
- ae.safetensors

放入 ComfyUI/models/unet/ 和 ComfyUI/models/vae/
```

### 5. 下载基础模型（可选 SDXL）
```
https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
放入 ComfyUI/models/checkpoints/
```

---

## 二、启动
```bash
python main.py
# 浏览器打开 http://127.0.0.1:8188
```

---

## 三、工作流
启动后导入 `/root/.openclaw/workspace/知识库/项目/维度黎明/短视频工作流.md` 中的工作流 JSON，或手动搭建。

---

## 四、风格模板使用
在 ComfyUI 的 K采样器 中使用《维度黎明的提示词模板，替换 `[描述]` 即可。

---

## 常见问题
- **显存不够**：降低分辨率或减少批次
- **速度慢**：使用 FLUX 的 Schnell 版本（fp16）
- **模型下载慢**：用抱脸下载加速

---

## 下一步
装好后告诉我，我来帮你搭建具体的工作流节点。