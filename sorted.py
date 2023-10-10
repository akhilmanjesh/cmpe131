
def sort_dictionary(d):
    sorted_list = sorted([(name, info[0]) for name, info in d.items()], reverse=True)
    return sorted_list
