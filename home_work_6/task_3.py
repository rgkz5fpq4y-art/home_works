import math


number = int(input("Enter yor number to see a magic multiplication: "))
while number >= 10:
    number = math.prod(int(digit) for digit in str(number))
print(number)



