"""simulate_random_walk 的单元测试。"""

from __future__ import annotations

import pytest

from dsh_demo import simulate_random_walk


def test_same_seed_is_reproducible() -> None:
    """相同 seed 的两次调用应当返回完全相同的轨迹。"""
    first = simulate_random_walk(steps=100, seed=42)
    second = simulate_random_walk(steps=100, seed=42)

    assert first == second


def test_different_seed_may_differ() -> None:
    """不同 seed 通常会得到不同的轨迹。"""
    first = simulate_random_walk(steps=100, seed=1)
    second = simulate_random_walk(steps=100, seed=2)

    assert first != second


def test_trajectory_length_and_start() -> None:
    """轨迹长度应为 steps + 1，且从 0 开始。"""
    steps = 20
    trajectory = simulate_random_walk(steps=steps, seed=7)

    assert len(trajectory) == steps + 1
    assert trajectory[0] == 0


def test_each_step_moves_by_one() -> None:
    """相邻两步之间的位置变化必须恰好为 +1 或 -1。"""
    trajectory = simulate_random_walk(steps=50, seed=123)

    for previous, current in zip(trajectory, trajectory[1:]):
        assert abs(current - previous) == 1


def test_zero_steps_returns_start_only() -> None:
    """步数为 0 时只返回起始位置。"""
    assert simulate_random_walk(steps=0, seed=0) == [0]


def test_negative_steps_raises() -> None:
    """负步数应抛出 ValueError。"""
    with pytest.raises(ValueError):
        simulate_random_walk(steps=-1, seed=0)


def test_non_integer_steps_raises() -> None:
    """非整数步数应抛出 TypeError。"""
    with pytest.raises(TypeError):
        simulate_random_walk(steps=1.5, seed=0)  # type: ignore[arg-type]
