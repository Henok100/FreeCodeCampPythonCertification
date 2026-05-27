# Budget App

A Python budgeting system that tracks spending across categories and visualizes spending distribution using a text-based bar chart.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Track deposits and withdrawals
- Transfer money between categories
- Calculate balances automatically
- Validate available funds
- Generate spending percentage chart

## Class: Category

Represents a budget category such as Food, Clothing, or Entertainment.

### Methods

- `deposit(amount, description)`
- `withdraw(amount, description)`
- `get_balance()`
- `transfer(amount, category)`
- `check_funds(amount)`
- `__str__()`

## Spending Chart

The `create_spend_chart()` function generates a vertical bar chart showing percentage of spending per category.

## Example Output

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Concepts Used

- Object-Oriented Programming
- Data structures (lists, dictionaries)
- String formatting
- Loops and conditionals
- Algorithm design
- Data visualization (text-based)