"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    sport_category = "Athlete"

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def display_info(self):
        return (
            f"Name: {self.name}, Team: {self.team}, "
            f"Category: {self.sport_category}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    league_name = "World Basketball League"

    def __init__(self, name, team, position, jersey_number):
        super().__init__(name, team)
        self.position = position
        self.jersey_number = jersey_number
        self.game_stats = []

    def record_game(self, opponent, points):
        # Handle a missing opponent or invalid point total.
        if not opponent:
            print("Game not recorded: opponent cannot be empty.")
            return

        if points < 0:
            print("Game not recorded: points cannot be negative.")
            return

        game = {
            "opponent": opponent,
            "points": points
        }

        self.game_stats.append(game)
        print(
            f"Recorded game against {opponent}: "
            f"{points} points."
        )

    #  extension that calculates scoring average.
    def calculate_scoring_average(self):
        if len(self.game_stats) == 0:
            return 0

        total_points = 0

        for game in self.game_stats:
            total_points += game["points"]

        return total_points / len(self.game_stats)

    def display_info(self):
        return (
            f"Name: {self.name}, Team: {self.team}, "
            f"Position: {self.position}, "
            f"Jersey Number: {self.jersey_number}, "
            f"League: {self.league_name}, "
            f"Games Recorded: {len(self.game_stats)}"
        )

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    player1 = ChildClass(
        "Jordan",
        "Canada Team",
        "Point Guard",
        3
    )

    player2 = ChildClass(
        "Cameron",
        "Canada Team",
        "Center",
        24
    )

    print(
        "League accessed through the class:",
        ChildClass.league_name
    )

    print(
        "League accessed through an object:",
        player1.league_name
    )

    # The captain attribute is added only to player1.
    player1.captain = True

    print("Player 1 instance namespace:", player1.__dict__)
    print("Player 2 instance namespace:", player2.__dict__)
    print("ChildClass namespace:", ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original_player = ChildClass(
        "Taylor",
        "Australia Team",
        "Shooting Guard",
        11
    )

    original_player.record_game("New Zealand Team", 18)

    shallow_player = copy(original_player)
    deep_player = deepcopy(original_player)

    # A shallow copy creates a new player object but continues
    # sharing the nested game_stats list with the original.
    original_player.record_game("Sudan Team", 22)

    #A deep copy creates a new player object with independent
    # nested data, so the added game does not appear in it.
    print("Original game statistics:", original_player.game_stats)
    print("Shallow copy statistics:", shallow_player.game_stats)
    print("Deep copy statistics:", deep_player.game_stats)



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object Test ===")
    athlete = ParentClass("Morgan", "USA TEAM")
    print(athlete.display_info())

    print("\n=== Child Object Test ===")
    basketball_player = ChildClass(
        "Devin",
        "USA Team",
        "Point Guard",
        5
    )

    print(basketball_player.display_info())

    basketball_player.record_game("Australia Team", 16)
    basketball_player.record_game("New Zealand Team", 24)

    print(
        f"Scoring average: "
        f"{basketball_player.calculate_scoring_average():.1f} points"
    )

    print("\n=== Edge-Case Tests ===")

    # Test a missing opponent.
    basketball_player.record_game("", 12)

    # Test an invalid negative point value.
    basketball_player.record_game("Sudan Team", -5)

    # Test the average calculation with no recorded games.
    new_player = ChildClass(
        "Alex",
        "New Zealand Team",
        "Forward",
        12
    )

    print(
        f"Average with no games: "
        f"{new_player.calculate_scoring_average():.1f} points"
    )


    demonstrate_namespaces()
    demonstrate_copying()




if __name__ == "__main__":
    main()