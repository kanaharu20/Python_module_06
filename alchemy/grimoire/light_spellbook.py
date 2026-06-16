def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    from .light_validator import validate_ingredients
    valid_or_invalid: str = validate_ingredients(ingredients)
    if valid_or_invalid.endswith("- VALID"):
        return (
            "Testing record light spell: Spell recorded: "
            f"{spell_name} ({valid_or_invalid})"
            )
    else:
        return (
            "Testing record light spell: Spell rejected: "
            f"{spell_name} ({valid_or_invalid})"
            )
