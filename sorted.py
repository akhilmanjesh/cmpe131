def sort_dictionary(d):
    sorted_list = sorted([(name, info[0]) for name, info in d.items()])
    return sorted_list
