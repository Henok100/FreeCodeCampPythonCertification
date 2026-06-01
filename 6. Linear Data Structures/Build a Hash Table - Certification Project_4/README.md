# Hash Table Implementation

A simple hash table data structure built from scratch in Python using a basic Unicode-based hashing function.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Custom hash function using Unicode values
- Collision handling using nested dictionaries
- Key-value storage system
- Add, remove, and lookup operations
- Safe handling of missing keys

## Class: HashTable

### Methods

#### `hash(string)`
Generates a hash value by summing Unicode values of characters.

#### `add(key, value)`
Adds a key-value pair to the hash table.

#### `remove(key)`
Removes a key-value pair if it exists.

#### `lookup(key)`
Returns the value associated with a key or `None`.

## Example Usage

```python
ht = HashTable()

ht.add("name", "Alice")
ht.add("age", 25)

print(ht.lookup("name"))
ht.remove("age")
```

## Concepts Used

- Data structures
- Dictionaries
- Hashing algorithms
- Collision handling
- Key-value storage systems
- Algorithm design