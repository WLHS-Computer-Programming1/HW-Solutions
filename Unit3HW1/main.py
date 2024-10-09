'''
Name: Brandon Smith
Date: 10-9-24
Assignment: Unit 3 HW 1
Description: Comparison of different if-elif layouts
'''

'''
Age     |   Category    |   Price
0-6         KITTEN          250
7-11        TEENAGER        225
12-95       ADULT           150
>96         SENIOR          85 
'''

cat_age = int(input("Enter the age of the cat in months: "))

# Approach 1 - is valid, produces good results

if cat_age <= 6:
    print(f"The price of the kitten is $250")
elif cat_age <= 11:
    print(f"The price of the teenager cat is $225")
elif cat_age <= 95:
    print(f"The price of the adult cat is $150")
elif cat_age >= 96:
    print(f"The price of the senior cat is $85")