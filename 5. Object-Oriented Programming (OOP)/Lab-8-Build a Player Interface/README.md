"""
Game Character Stats Tracker

A simple RPG-style character system that manages
health, mana, and leveling mechanics using properties.

This project was completed as part of the freeCodeCamp Python Certification.
"""


class GameCharacter:
    """
    Represent a game character with health, mana, and level stats.
    """

    def __init__(self, name):
        """
        Initialize a new game character.

        Args:
            name (str): Character name.
        """

        self._name = name
        self.health = 100
        self.mana = 50
        self._level = 1

    @property
    def name(self):
        """
        Read-only access to character name.
        """
        return self._name

    @property
    def health(self):
        """
        Get current health value.
        """
        return self._health

    @health.setter
    def health(self, value):
        """
        Set health value between 0 and 100.
        """

        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        """
        Get current mana value.
        """
        return self._mana

    @mana.setter
    def mana(self, value):
        """
        Set mana value between 0 and 50.
        """

        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        """
        Get current character level.
        """
        return self._level

    def level_up(self):
        """
        Increase character level and restore stats.
        """

        self._level += 1
        self.health = 100
        self.mana = 50

        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        """
        Return formatted character stats.
        """

        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )