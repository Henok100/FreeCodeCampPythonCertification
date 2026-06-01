# RPG Character Creator

A Python function that creates and validates RPG characters using customizable stats and visual stat bars.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Character name validation
- Stat validation system
- Point allocation rules
- Visual stat display using Unicode symbols
- RPG-style character formatting

## Validation Rules

### Character Name
- Must be a string
- Cannot be empty
- Cannot contain spaces
- Maximum length: 10 characters

### Stats
- Must be integers
- Must be between 1 and 4
- Total stat points must equal 7

## Example Usage

```python
print(create_character("Knight", 3, 2, 2))
```

## Example Output

```text
Knight
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```

## Concepts Used

- Functions
- Input validation
- Conditional logic
- String formatting
- Unicode characters
- Multiline string construction