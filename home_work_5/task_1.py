import string
import keyword


print(string.punctuation)
print(keyword.kwlist)


variable_name = str(input("Please input your variable name: "))
is_valid = True
if variable_name in keyword.kwlist:
    is_valid = False
elif variable_name[0].isdigit():
    is_valid = False
elif "__" in variable_name:
    is_valid = False
for char in variable_name:
    if char in string.punctuation and char != "_":
        is_valid = False
        break
    elif char == " " or char.isupper():
        is_valid = False
print(is_valid)

