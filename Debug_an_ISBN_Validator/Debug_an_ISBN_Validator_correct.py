"""
Python ISBN Validator

A program that validates ISBN-10 and ISBN-13 codes by
calculating and verifying their check digits.

This project was completed as part of the freeCodeCamp
Python Certification debugging labs.
"""

def validate_isbn(isbn, length):
    """
    Validate an ISBN code using its calculated check digit.

    Args:
        isbn (str): The ISBN code entered by the user.
        length (int): Expected ISBN length (10 or 13).
    """

    # Ensure the ISBN has the correct length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    # Separate main digits from the check digit
    main_digits = isbn[0:length - 1]
    given_check_digit = isbn[length - 1]

    main_digits_list = [int(digit) for digit in main_digits]
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    """
    Calculate the check digit for an ISBN-10 code.

    Args:
        main_digits_list (list): First 9 digits of ISBN-10.

    Returns:
        str: Calculated check digit.
    """

    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    """
    Calculate the check digit for an ISBN-13 code.

    Args:
        main_digits_list (list): First 12 digits of ISBN-13.

    Returns:
        str: Calculated check digit.
    """

    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    """
    Handle user input and validate ISBN codes.
    """

    user_input = input('Enter ISBN and length: ')
    
    # Handle invalid user input without crashing the program
    try:
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])

    except IndexError:
        print("Enter comma-separated values.")
        return

    except ValueError:
        print("Length must be a number.")
        return

    # Validate ISBN-10 characters        
    if length == 10:
        if not (isbn[:9].isdigit() and (isbn[9].isdigit() or isbn[9] == 'X')):
            print("Invalid character was found.")
            return

    # Validate ISBN-13 characters
    if length == 13:
        if not isbn.isdigit():
            print("Invalid character was found.")
            return


    # Accept only ISBN-10 or ISBN-13 lengths
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

main()