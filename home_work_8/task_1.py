def add_one(some_list):
    list1 = "".join(str(x) for x in some_list)
    result = [int(x) for x in str(int(list1) + 1)]
    return result
print(add_one([1, 2, 3, 4]))


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")