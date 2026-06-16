import elements as top_elements

import alchemy.elements as bottom_elements


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{bottom_elements.create_earth()}'"
        f" and '{bottom_elements.create_air()}'"
        )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{top_elements.create_fire()}'"
        f" and '{top_elements.create_water()}'"
        )
