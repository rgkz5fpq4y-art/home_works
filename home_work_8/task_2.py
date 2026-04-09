def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "").replace(",", "").replace(":", "").replace(".", "")
    if text == text[::-1]:
        return True
    else:
        return False
print(is_palindrome("A man, a plan, a canal: Panama"))




assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")