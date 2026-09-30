# dsh-demo

一个用于演示 Python 项目结构的示例代码库，提供一维随机游走（Random Walk）的模拟功能。

## 项目简介

本项目是一个最小化的 Python 示例工程，采用 `src` 布局，包含：

- 一个可复用的核心函数 `simulate_random_walk(steps, seed)`，用于模拟一维随机游走并返回轨迹列表；
- 基于 `pytest` 的单元测试，验证相同随机种子下结果的可重复性；
- 标准的 `pyproject.toml` 打包配置，要求 Python >= 3.10。

## 环境要求

- Python >= 3.10

## 安装

推荐使用虚拟环境进行安装：

```bash
# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate

# 以可编辑模式安装项目（含测试依赖）
pip install -e ".[test]"
```

如果只想安装运行时依赖：

```bash
pip install -e .
```

## 使用说明

安装完成后，即可在 Python 中调用核心函数：

```python
from dsh_demo import simulate_random_walk

# 模拟 10 步随机游走，随机种子为 42
trajectory = simulate_random_walk(steps=10, seed=42)
print(trajectory)

# 相同的 seed 会得到完全相同的结果（可重复性）
assert simulate_random_walk(steps=10, seed=42) == trajectory
```

`simulate_random_walk` 的返回值为一个长度为 `steps + 1` 的列表，第一个元素为起始位置 `0`，后续元素为每一步移动后的位置。

## 运行测试

```bash
pytest
```

## 目录结构

```
dsh-demo/
├── README.md
├── pyproject.toml
├── .gitignore
├── src/
│   └── dsh_demo/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
```
