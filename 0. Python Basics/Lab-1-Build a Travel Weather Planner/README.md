# Travel Weather Planner

A simple Python program that determines whether commuting is possible based on weather conditions, travel distance, and available transportation options.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Evaluates commuting feasibility based on distance
- Considers weather conditions (rain)
- Supports multiple transport options (bike, car, ride-share)
- Uses conditional logic (if/elif/else)

## Logic Rules

- If distance is 0 or empty → cannot commute
- ≤ 1 mile → allowed only if not raining
- 1–6 miles → allowed only with a bike and no rain
- > 6 miles → allowed if car or ride-share is available

## Concepts Used

- Boolean logic
- Conditional statements
- Decision-making algorithms

## Example

```python
distance_mi = 5
is_raining = False
has_bike = True

# Output: True
```

## What I Learned

- How to build decision-based logic systems
- How to structure nested conditions clearly
- How to model real-world decisions in Python