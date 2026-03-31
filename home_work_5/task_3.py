import string


mystring = input("Please enter a string: ")
hashtag = mystring.title()
clean_hashtag = ""
for char in hashtag:
    if char not in string.punctuation and char != " ":
        clean_hashtag += char
result = "#" + clean_hashtag
print(result[:140])
