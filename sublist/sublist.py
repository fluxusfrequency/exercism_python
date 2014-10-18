def check_lists(l1, l2):
    if (l1 == l2):
        return EQUAL
    elif (__is_sublist(l1, l2)):
        return SUBLIST
    elif (__is_sublist(l2, l1)):
        return SUPERLIST
    else:
        return UNEQUAL


def __is_sublist(l1, l2):
    if not l1:
        return True
    result = True
    for val in l1:
        if val not in l2:
            result = False
    return result

SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'
