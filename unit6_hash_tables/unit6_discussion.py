"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")

    # This dictionary works like a hash table by storing
    # reservation names as keys and party sizes as values.
    # Each key must be unique and can be used to quickly
    # access the value connected to that key.
    reservations = {}

    reservations["Smith"] = 4
    reservations["Terry"] = 2
    reservations["Green"] = 6
    reservations["Buford"] = 3
    reservations["Woods"] = 5

    print("Current reservations:")
    print(reservations)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary lookup uses the key to find the value
    # associated with that reservation.

    print("Smith reservation party size:", reservations["Smith"])
    print("Green reservation party size:", reservations["Green"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(reservations)

    # Since "Terry" already exists as a key, assigning a new
    # value updates the existing reservation instead of creating
    # a duplicate key.

    reservations["Terry"] = 4

    print("After updating Terry's party size:")
    print(reservations)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(reservations)

    # Removing a key also removes the value associated with it.
    del reservations["Buford"]

    print("After deleting Buford's reservation:")
    print(reservations)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Looking up a missing key with get().
    # get() safely returns a default value instead of causing an error.
    missing_reservation = reservations.get("Taylor", "Reservation not found")
    print("Looking up Taylor:", missing_reservation)

    # Edge case 2: Safely removing a key that does not exist.
    # pop() can use a default value so the program does not crash.
    removed_reservation = reservations.pop("Anderson", "Reservation not found")
    print("Removing Anderson:", removed_reservation)

    print("\nFinal reservations:")
    print(reservations)

if __name__ == "__main__":
    main()