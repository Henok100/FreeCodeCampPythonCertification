# Player Interface - RPG Movement System

A Python implementation of an abstract player system using OOP principles, randomness, and movement logic.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Abstract base class using `ABC`
- Random movement system
- Position tracking
- Path history logging
- Extensible player design
- Inheritance and polymorphism

## Classes

### Player (Abstract Class)

Defines the base behavior for all game characters:
- Movement system
- Position tracking
- Path history
- Abstract `level_up()` method

### Pawn (Concrete Class)

A playable character that:
- Moves in 4 directions initially
- Gains diagonal movement after leveling up

## Methods

### make_move()
Randomly selects a move and updates position.

### level_up()
Adds new diagonal movement options.

## Example Usage

```python
pawn = Pawn()

pawn.make_move()
pawn.level_up()
pawn.make_move()

print(pawn.position)
print(pawn.path)
```

## Concepts Used

- Abstract classes
- Inheritance
- Polymorphism
- Random module
- State tracking
- Game movement logic