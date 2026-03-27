lst = [0,0,0,0,5,6,0,3,9,0,8,0,4563,0]
new_lst = [item for item in lst if item != 0] + [item for item in lst if item == 0]
print(new_lst)
