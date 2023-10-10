def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Invalid input"

    merged = list1 + list2

    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
    
    return merged

