def count_occurrences_of_max_value(arr):
    if not arr:
        return 0
    max_elem = max(arr)
    return arr.count(max_elem)
