"""
Author: Sabrina Joseph
Date: 01-31-2024
Last Modified: 01-31-2024
Description: Lab 3 - Scientific Calculator
"""
import math

curr_result = float(0.0)
output = 0
num = 0
total = 0

print(f"Current Result: {curr_result}\n")
# Having this here to ensure the program continuously runs unless a break statement
while True:

    # Introduction to the calculator
    print("Calculator Menu\n--------------- ")
    print("0. Exit Program\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exponentiation\n"
          "6. Logarithm\n"
          "7. Display Average")

    # User menu selection
    menu = int(input("Enter Menu Selection: "))

    while menu != 0 and menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6 and menu != 7:
        print("Error: Invalid selection!\n")
        menu = int(input("Enter Menu Selection: "))
        continue

    while menu == 7:
        if num == 0:
            # checking for the first error of asking for the average without list of outputs
            print("Error: No calculations yet to average!\n")
            menu = int(input("Enter Menu Selection: "))
            continue
        else:
            print(f"\nSum of calculations: {round(total, 2)}")
            print(f"Number of calculations: {round(num, 2)}")
            print(f"Average of calculations: {round(total/num, 2)}\n")
            break

    # performing operations based on user selection
    while 1 <= menu <= 6:
        op1 = float(input("Enter first operand: "))
        op2 = float(input("Enter second operand: "))

        # 1 - Addition
        if menu == 1:
            output = op1 + op2
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        # 2 - Subtraction
        elif menu == 2:
            output = op1 - op2
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        # 3 - Multiplication
        elif menu == 3:
            output = op1 * op2
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        # 4 - Division
        elif menu == 4:
            output = op1 / op2
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        # 5 - Exponentiation
        elif menu == 5:
            output = op1**op2
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        # 6 - Logarithm
        elif menu == 6:
            output = math.log(op2, op1)
            curr_result = output
            print(f"\nCurrent Result: {round(curr_result, 2)}\n")

        break

    # adding 1 to the number of rounds and adding outputs together
    num += 1
    total += output

    # ending the program per user's command
    if menu == 0:
        print("\nThanks for using this calculator. Goodbye!")
        break
