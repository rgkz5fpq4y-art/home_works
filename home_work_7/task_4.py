def common_elements():
    list1 = [x for x in range(100) if x % 3 == 0]
    list2 = [x for x in range(100) if x % 5 == 0]
    list1, list2 = set(list1), set(list2)
    result = list1.intersection(list2)
    return result
print(common_elements())

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")

