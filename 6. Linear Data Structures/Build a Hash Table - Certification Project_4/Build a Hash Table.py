"""
Hash Table Implementation

A simple hash table data structure that stores key-value pairs
using a basic hashing function based on Unicode character sums.

This project was completed as part of the freeCodeCamp Python Certification.
"""


class HashTable:
    """
    A basic hash table implementation using Python dictionaries.
    """

    def __init__(self):
        """
        Initialize an empty hash table.
        """
        self.collection = {}

    def hash(self, string):
        """
        Generate a hash value for a string key.

        The hash function sums the Unicode values of all characters.

        Args:
            string (str): The key to hash.

        Returns:
            int: Computed hash value.
        """
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.

        Args:
            key (str): Key to store.
            value (any): Value associated with the key.
        """
        hash_value = self.hash(key)

        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        """
        Remove a key-value pair from the hash table if it exists.

        Args:
            key (str): Key to remove.
        """
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key):
        """
        Retrieve a value from the hash table.

        Args:
            key (str): Key to search for.

        Returns:
            any or None: Value if found, otherwise None.
        """
        hash_value = self.hash(key)

        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]

        return None