def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    result_index = text.find(some_str, first_index +1)
    if result_index == -1:
        return None
    return result_index
print(second_index("sims", "h"))

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')