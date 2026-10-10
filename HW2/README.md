# Trail Supply Planner

Write a program that helps a hiker plan water and weather gear for a day hike. Use variables, arithmetic, functions, conditionals, Boolean expressions, `input()`, `print()`, and f-strings.

The program must:

1. Ask for the trail distance, temperature, whether rain is expected, and whether it will be sunny. Use `y` or `n` for the weather questions.
2. Accept distances from 1 through 30 miles and temperatures from 0 through 100 degrees. Print a specific error and stop the plan if an input is invalid.
3. Define `calculate_water(distance, temperature)`. Recommend 0.25 liters per mile plus one extra liter when the temperature is above 80 degrees.
4. Define `print_gear_advice(is_raining, is_sunny, temperature)` and print every recommendation that applies:
   - Rain: pack a rain jacket.
   - Sun: pack sunscreen and a hat.
   - Below 40 degrees: pack an insulated layer.
   - From 40 through 70 degrees: pack a light extra layer.
5. Print the water amount to two decimal places and print the gear advice.
6. Test these cases: 8 miles at 85 degrees with rain and sun; 4 miles at 40 degrees with sun; an invalid distance of 0 miles; and 10 miles at 20 degrees with rain.

## What This Problem Assesses

This problem assesses input validation, compound conditions, and functions. It also tests the difference between an `if`/`elif` chain and separate `if` statements. The temperature ranges are mutually exclusive, but rain and sun can both be true.

The hardest part is organizing the conditions so every boundary is handled correctly and all applicable advice is printed. Completing it gives practice turning written rules into accurate Boolean expressions.

## Answer Key

The complete answer is in `solution.py`.

- 8 miles, 85 degrees, rain and sun: 3.00 liters, rain jacket, sunscreen, and hat.
- 4 miles, 40 degrees, no rain and sun: 1.00 liter, sunscreen, hat, and a light layer.
- 0 miles: invalid-distance message and no plan.
- 10 miles, 20 degrees, rain and no sun: 2.50 liters, rain jacket, and an insulated layer.
