from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    for ingr in light_spell_allowed_ingredients():
        if ingr in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
