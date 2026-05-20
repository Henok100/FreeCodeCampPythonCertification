"""
RPG Character Creator

A simple Python program that creates and validates RPG characters
using customizable stats and visual stat bars.

This project was completed as part of the freeCodeCamp Python Certification.
"""

full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    """
    Create and validate an RPG character.

    Args:
        name (str): Character name.
        strength (int): Strength stat.
        intelligence (int): Intelligence stat.
        charisma (int): Charisma stat.

    Returns:
        str: Character profile or validation error message.
    """

    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stat types
    if (
        not isinstance(strength, int)
        or not isinstance(intelligence, int)
        or not isinstance(charisma, int)
    ):
        return "All stats should be integers"

    # Validate minimum stat values
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # Validate maximum stat values
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Ensure total stat points equal 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Build character profile
    return (
        f"{name}\n"
        f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
        f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
        f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    )