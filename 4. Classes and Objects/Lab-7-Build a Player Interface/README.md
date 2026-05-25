# Game Character Stats Tracker

A Python class that models an RPG game character with health, mana, and leveling mechanics.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Object-oriented character system
- Encapsulation using private attributes
- Property getters and setters
- Automatic stat validation and capping
- Character leveling system
- Custom string representation

## Class Overview

### `GameCharacter(name)`

Creates a character with:
- Health = 100
- Mana = 50
- Level = 1

## Properties

- `name` → read-only character name
- `health` → capped between 0 and 100
- `mana` → capped between 0 and 50
- `level` → current character level

## Methods

### `level_up()`
- Increases level by 1
- Restores health and mana
- Prints level-up message

### `__str__()`
Returns formatted character information.

## Example Usage

```python
hero = GameCharacter("Kratos")

print(hero)

hero.level_up()
```

## Example Output

```text
Name: Kratos
Level: 1
Health: 100
Mana: 50
```

## Concepts Used

- Classes and objects
- Encapsulation
- Properties
- Getters and setters
- State management
- Object-oriented programming
