# def flatten_list(nested_list):
#     result = []
# (Outer Loop) Use for loop to iterate through each item in the collection
# (Inner Loop) Need to handle False and add int to result
# (Inner Loop) Need to handle True (if it's a nested list)
# (Inner Loop) If find nested list, call function again to iterate through that sub-list
# Use extend for true condition to add to result list
# Use append for false condition to add straight integer to result list
# Need to return result and print

def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def flatten_list_gmo(nested_list, result=None):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


print(flatten_list([1, 2, [3], [4, 5]]))
print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))

print(flatten_list_gmo([1, 2, [3], [4, 5]]))
print(flatten_list_gmo([1, [2], [3, [4, 5, [6]]], 7]))
