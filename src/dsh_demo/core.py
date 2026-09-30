"""核心模拟逻辑。"""

from __future__ import annotations

import random


def simulate_random_walk(steps: int, seed: int) -> list[int]:
    """模拟一维随机游走并返回轨迹列表。

    在每一步中，游走者以相等的概率向左（-1）或向右（+1）移动一步。
    使用给定的 ``seed`` 初始化随机数生成器，因此对于相同的
    ``steps`` 和 ``seed``，返回的轨迹完全一致（可重复）。

    Args:
        steps: 游走的步数，必须为非负整数。
        seed: 随机数种子，用于保证结果可重复。

    Returns:
        长度为 ``steps + 1`` 的轨迹列表。第一个元素恒为起始位置 ``0``，
        之后每个元素是移动后的累计位置。

    Raises:
        TypeError: 当 ``steps`` 或 ``seed`` 不是整数时。
        ValueError: 当 ``steps`` 为负数时。
    """
    if not isinstance(steps, int) or isinstance(steps, bool):
        raise TypeError(f"steps 必须是整数，而不是 {type(steps).__name__}")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise TypeError(f"seed 必须是整数，而不是 {type(seed).__name__}")
    if steps < 0:
        raise ValueError("steps 必须是非负整数")

    rng = random.Random(seed)

    position = 0
    trajectory = [position]
    for _ in range(steps):
        position += rng.choice((-1, 1))
        trajectory.append(position)

    return trajectory
