lst = [0, 1, 7, 2, 4, 8]
if len(lst) == 0:
    print(0)
else:
    x = [lst[i] for i in range(0,len(lst),2)]
    result = sum(x) * lst[-1]
    print(result)
