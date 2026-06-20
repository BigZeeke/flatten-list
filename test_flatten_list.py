from flatten_list import flatten_list


def run_tests(flatten_list):
    assert flatten_list([1, 2, [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_list([1, [2], [3, [4, 5, [6]]], 7]) == [
        1, [2], [3, [4, 5, [6]]], 7]
    assert flatten_list([2, ["two"], 3]) == [2, "two", 3]


print("All tests passed")
print(flatten_list([1, 2, [3], [4, 5]]))
print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))
print(flatten_list([2, ["two"], 3]))
