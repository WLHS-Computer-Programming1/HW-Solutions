from streamlit import area_chart


def print_product(a,b):
    print(a*b)

def print_multiple_times(string,n):
    for i in range(n):
        print(string)

def calculate_area(side_length=10):
    square_area= side_length**2
    print(f"The area of a square with sides of length {side_length} is {square_area}.")

def main():
    print_product(5,7)
    print_multiple_times("hi",3)
    side_length = int(input("Enter side length: "))
    if side_length > 0:
        calculate_area(side_length)
    else:
        calculate_area()

if __name__ == '__main__':
    main()