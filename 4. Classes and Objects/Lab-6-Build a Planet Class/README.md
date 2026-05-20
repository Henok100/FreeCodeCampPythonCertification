# Planet Class

A Python class that models planets, validates planet data, and simulates orbital behavior.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Object-oriented programming (OOP)
- Input validation using exceptions
- Custom string representation with `__str__`
- Planet orbit simulation
- Reusable class structure

## Class Overview

### `Planet(name, planet_type, star)`

Creates a planet object with:
- Name
- Planet type
- Associated star

## Methods

### `orbit()`
Returns a description of the planet orbiting its star.

### `__str__()`
Returns a formatted string representation of the planet.

## Example Usage

```python
earth = Planet("Earth", "Terrestrial", "Sun")

print(earth)
print(earth.orbit())
```

## Example Output

```text
Planet: Earth | Type: Terrestrial | Star: Sun
Earth is orbiting around Sun...
```

## Concepts Used

- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Exception handling
- Magic methods (`__str__`)
- Object-oriented programming