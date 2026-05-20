lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = [item for item in lst if item != 0] + [item for item in lst if item == 0]
print(new_lst)
