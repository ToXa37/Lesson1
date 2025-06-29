def move_last_to_first(lst):
    if len(lst) > 1:
        last_element = lst[-1]
        lst.insert(0, last_element)
        lst.pop()
    return lst

test_list = [
    ([12, 3, 4, 10], [10, 12, 3, 4]),
    ([1], [1]),
    ([], []),
    ([12, 3, 4, 10, 8], [8, 12, 3, 4, 10])
]

for input_list, expected_output in test_list:
    result = move_last_to_first(input_list.copy())
    print(f"{input_list} => {result} | {'True' if result == expected_output else 'False'}")