def calculate_total_cost(meal_cost,tip=15):
    return meal_cost * (1+tip/100)

def main():
    while True:
        try:
            meal_cost = float(input("Enter the meal cost: "))
            meal_tip = int(input("Enter the tip percentage: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for meal cost and tip percentage.")
            continue

        if meal_tip<0:
            print("Invalid tip percentage! Using default value.")
            total = calculate_total_cost(meal_cost)
            print(f"The total cost of the meal is ${total:.2f}")
        else:
            total = round(calculate_total_cost(meal_cost), 2)
            print(f"The total cost of the meal is ${total:.2f}")

if __name__ == '__main__':
    main()
