# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation

I created a restaurant reservation system using a Python dictionary to represent a hash table. The customer's last name was used as the key and the party size was used as the value. I added five reservations using the names Smith, Terry, Green, Buford, and Woods.

I also demonstrated lookup, update, and delete operations. For the lookup operation, I used existing customer names to retrieve their party sizes. For the update operation, I changed Terry's party size from 2 to 4. Since Terry was already a key in the dictionary, Python updated the existing value instead of creating a duplicate entry. For the delete operation, I removed Buford from the reservation system.

Python dictionaries behave like hash tables because they use keys to quickly locate values. Instead of checking every reservation one at a time, the dictionary uses the key to determine where the information should be stored and retrieved. On average, dictionary insert, lookup, and delete operations have O(1) time complexity.

## Testing and Edge Cases

I tested the dictionary by adding five reservations and then looking up two existing customers. The program correctly returned the party size associated with Smith and Green.

I also tested updating an existing key. Terry originally had a party size of 2, and I changed the value to 4. The dictionary kept only one Terry entry and updated the value instead of creating a duplicate key.

For the edge cases, I tested looking up a reservation that did not exist. I used the get() method to search for Taylor, and the program returned "Reservation not found" instead of causing an error.

I also tested deleting a key that did not exist. I used pop() with a default value to attempt to remove Anderson. Since Anderson was not in the dictionary, the program returned "Reservation not found" and continued running normally.

## Discussion Board Reflection

While completing this assignment, I learned more about how Python dictionaries can be used like hash tables to store key-value pairs. Dictionaries make it possible to quickly find a value using its key, and keys must be unique. If an existing key is given a new value, the old value is updated instead of creating a duplicate.

One challenge I had was understanding how collisions are handled when different keys map to the same location in a hash table. I learned that Python handles these collisions internally, so I did not have to manage them myself in this program. 

A real-world example would be a restaurant reservation system. A customer's name or reservation number could be used as the key and the party size as the value. This would allow the restaurant to quickly find and update reservations during busy hours. Hash tables can perform insert, lookup, and delete operations in 0(1) average time, which makes them useful when information needs to be accessed quickly.

