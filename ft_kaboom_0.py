#!/usr/bin/env python3
import alchemy.grimoire as grimoire


def test() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire"
        ))


if __name__ == "__main__":
    test()
