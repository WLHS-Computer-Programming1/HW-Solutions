'''Write code that will calculate how much it will cost someone to drive from Portland to
Seattle which is 173.8 miles. Here are possible steps:

Store the distance to Seattle in a variable
Ask the user how many miles per gallon their car gets and store the value. This value should be a whole number.
Ask the user how much a gallon of gas is near their house and store the value. This value can be a whole number or decimal
Ask the user how many gallons of gas their car holds (typical values are between 12 and 18). This value should be an integer.
Calculate the cost to drive 173.8 miles assuming they have to completely fill their car’s gas tank

Bonus: Assume the user’s tank was not empty. After step 4, ask them what fraction of their tank they had to fill up then calculate the cost of the trip.'''

dist_to_seattle = 173.8
mpg = int(input("What is your mpg? "))
cost_per_gallon = float(input("How much does gas cost near your house? "))
# extra credit: current_gallons = float(input("How many gallons of gas do you have in your car? "))
tank_capacity = int(input("How many gallons of gas can your car hold? (usually 12-18) "))
cost_to_fill_tank = cost_per_gallon * tank_capacity
# extra credit: gas_to_full = tank_capacity - current_gallons
gallons_to_seattle = dist_to_seattle / mpg # gallons to drive 173.8 miles
cost_to_seattle = gallons_to_seattle * cost_per_gallon
print(f"It cost you ${cost_to_fill_tank:.2f} to fill your car with gas.\n"
      f"${cost_to_seattle:.2f} of that was spent driving to Seattle.")

