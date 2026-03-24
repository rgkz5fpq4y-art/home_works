number_1 = float(input("Enter your first number: "))
number_2 = float(input("Enter your second number: "))
operator = input("Enter your operator (+, -, *, /):  ")
if operator == "+":
    print("The sum is: ", (number_1 + number_2))
elif operator == "-":
    print("The difference is: ", (number_1 - number_2))
elif operator == "*":
    print("The product is: ", (number_1 * number_2))
elif operator == "/" and number_2 == 0:
    print("You can't divide by zero")
elif operator == "/":
    print("The quotient is: ", (number_1 / number_2))
else:
    print("Please try again")


