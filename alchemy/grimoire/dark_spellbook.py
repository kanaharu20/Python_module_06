from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str):
    valid_or_invalid: str = validate_ingredients(ingredients)
    if valid_or_invalid.endswith("- VALID"):
        return (
            "Testing record dark spell: Spell recorded: "
            f"{spell_name} ({valid_or_invalid})"
            )
    else:
        return (
            "Testing record dark spell: Spell rejected: "
            f"{spell_name} ({valid_or_invalid})"
            )
