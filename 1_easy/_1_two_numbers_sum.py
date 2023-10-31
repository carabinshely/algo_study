from collections import defaultdict


def two_numbers_sum_a(list_, goal):
    for i in range(len(list_)-1):
        for j in range(i+1, len(list_)):
            if list_[i]+list_[j] == goal:
                return [list_[i], list_[j]]
    return None


def two_numbers_sum_b(list_, goal):
    diff_index_dict = defaultdict(list)
    for j, y in enumerate(list_):
        diff_index_dict[y].append(j)

    for i, x in enumerate(list_):
        if goal-x in diff_index_dict:
            indexes = diff_index_dict[goal-x]
            if i in indexes:
                indexes.remove(i)
            if len(indexes) > 0:
                return [x, list_[indexes[0]]]
    return None


def two_numbers_sum_c(list_, goal):
    diff_index_dict = set()
    for x in list_:
        if goal-x in diff_index_dict:
            return [goal-x, x]
        else:
            diff_index_dict.add(x)
    return None


