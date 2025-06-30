def split_list(lst):
    length = len(lst)
    if length == 0:
        return [[], []]

    split_index = (length + 1) // 2 
    return [lst[:split_index], lst[split_index:]]

test_lists = [
    ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
    ([1, 2, 3], [[1, 2], [3]]),
    ([1, 2, 3, 4, 5], [[1, 2, 3], [4, 5]]),
    ([1], [[1], []]),
    ([], [[], []])
]

for input_list, expected_output in test_lists:
    result = split_list(input_list)
    print(f"{input_list} => {result} | {'True' if result == expected_output else 'False'}")