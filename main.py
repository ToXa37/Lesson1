lst = [1, 2, 3, 4, 5, 6,7]

length = len(lst)
if length == 0:
    result = [[], []]
else:
    middle = (length + 1) // 2
    result = [lst[:middle], lst[middle:]]

print(result)