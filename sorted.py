
def sort_dictionary(d):
    sorted_list = sorted([(name, info[0]) for name, info in d.items()])
    return sorted_list

# test_dict = {'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}
# print(sort_dictionary(test_dict))
