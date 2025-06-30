lst = [0, 1, 0, 12, 3]
non_zeros = [x for x in lst if x != 0]
lst = non_zeros + [0] * (len(lst) - len(non_zeros))
print(lst)