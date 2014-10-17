def primitive_triplets(b):
    if not b % 2 == 0:
        return
    m, n = 0, 0
    while m < 10:
        while n < 10:
            if m > n and ((m -n) & 1 and True or False) and b / 2 == m * n:
                a = ((m ** 2) - (n ** 2))
                c = ((m ** 2) + (n ** 2))
                return set([(a, b, c)])
            n += 1
        m += 1
    return set([(a, b, c)])

def triplets_in_range(n):
    return True

def is_triplet(n):
    return True
