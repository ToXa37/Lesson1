test_list = [
    ([12, 3, 4, 10], [10, 12, 3, 4]),
    ([1], [1]),
    ([], []),
    ([12, 3, 4, 10, 8], [8, 12, 3, 4, 10])
]

for input_list, expected_output in test_list:
    if len(input_list) > 1:
        last_element = input_list[-1]
        result = [last_element] + input_list[:-1]
    else:
        result = input_list[:]

    print(f"{input_list} => {result} | {'True' if result == expected_output else 'False'}")