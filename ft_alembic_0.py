#!/usr/bin/env python3

import elements


def test() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    test()
