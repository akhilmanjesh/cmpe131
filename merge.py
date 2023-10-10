def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Expected inputs to be of type list")

    for lst in [list1, list2]:
        for item in lst:
            if not isinstance(item, int):
                raise TypeError("All elements in the lists should be integers")

    merged = list1 + list2

    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
    
    return merged
