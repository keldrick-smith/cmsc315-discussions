# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation

I created a parent class that represented a general athlete and stored the athlete's name and team. I created a child class that inherited this information and added a basketball player's position, jersey number, league, and game statistics. I overrode the parent's `display_info()` method to display the additional player information. I also added methods that recorded games and calculated a player's scoring average.
The game statistics were stored in a list of dictionaries. The list grew by one dictionary whenever a valid game was recorded. The shallow copy shared this nested list with the original player, while the deep copy created independent nested data and required additional memory.

## Testing and Edge Cases

I tested valid game records, an empty opponent, a negative point total, and a player with no recorded games. The program rejected invalid records and returned a zero scoring average when the game list was empty. This prevented invalid statistics and division-by-zero errors. The design could be used in a larger sports application for tracking teams, player performance, and scoring averages.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.