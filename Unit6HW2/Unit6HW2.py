"""
Name: Smith
Date: 12/16/24
Description: This function determines if a string represents a valid integer
"""

def is_integer(string:str)->bool:
    """
    Ignore white space in front and back, length has to be one,
    only digits, can have +/- as first character
    :param string:
    :return True if a valid integer, False if not:
    """
    string = string.strip()
    digits = "0123456789"
    valid_symbols = "+-"
    if not(string[0] in valid_symbols or string[0] in digits):
        return False
    for i in range(1,len(string)):
        if string[i] not in digits:
            return False
    return True

def main():
    print(is_integer("1234 567"))
    print(is_integer("12+81"))
    print(is_integer("+9037"))
    print(is_integer("-9036"))
    print(is_integer("   09823409029384             "))
    print(is_integer("+3987*&908"))

if __name__ == '__main__':
    main()