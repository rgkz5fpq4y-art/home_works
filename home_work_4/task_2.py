lst = [1,2,3,4,5]
if len(lst) == 0:
    print(0)
else:
    x = [lst[i] for i in range(0,len(lst),2)]
    result = sum(x) * lst[-1]
    print(result)
