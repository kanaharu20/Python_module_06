from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    for ingr in dark_spell_allowed_ingredients():
        if ingr in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
