# Problem:

Write a program that calculates and prints the total cost of a meal, including a tip. The user will provide the meal cost and optionally a tip percentage. If the user provides an invalid tip percentage (less than 0), use a default tip percentage of 15%. Use 15 rather than 0.15.

# Key steps:

1) Write a function called calculate_total_cost(...) that takes two parameters that are not shown here.
2) To calculate a meal with tip you multiply the meal cost by 1 + (tip/100) where tip is not in decimal form. Return the total cost.

3) In the main program, ask the user to input the meal cost as a float and the tip percentage as an integer.
4) If the user provides an invalid tip percentage (less than 0), call the function with the default tip percentage. Otherwise, call the function with the provided tip percentage.

5) If the user enters a tip or meal price that is non-numeric, print "Invalid input" and prompt them to enter both again.

6) Print the total cost, formatted to two decimal places (use round).

Here is some template code to get you started:

```python
def calculate_total_cost(....):

    # code to calculate meal cost


# get user input

meal_cost =

meal_ tip =

# determine how to call function
```

# Sample Input/Output

## Normal input
```
Enter the meal cost: 50
Enter the tip percentage: 20
The total cost of the meal is: $60.00
```

## Negative tip
```
Enter the meal cost: 50
Enter the tip percentage: -5
Invalid tip percentage! Using default value.
The total cost of the meal is: $57.50
```

## Non-numeric inputs
```
Enter the meal cost: abc
Invalid input. Please enter numeric values for meal cost and tip percentage.
Enter the meal cost: 50
Enter the tip percentage: xyz
Invalid input. Please enter numeric values for meal cost and tip percentage.
Enter the meal cost: 50
Enter the tip percentage: 10
The total cost of the meal is: $55.00

```
## Zero tip
```
Enter the meal cost: 30
Enter the tip percentage: 0
The total cost of the meal is: $30.00

```