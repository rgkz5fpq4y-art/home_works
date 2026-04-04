from string import ascii_letters


print(ascii_letters)
mystring = input("Enter your 2 letters from ASCII: ")
start = mystring[0]
end = mystring[-1]
start_index = ascii_letters.find(start)
end_index = ascii_letters.find(end)
print(ascii_letters[start_index:end_index+1])

