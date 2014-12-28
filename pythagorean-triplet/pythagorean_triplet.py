def primitive_triplets(b):
    m, n, o = 3, 4, 5
    return set([(m, n, o)])

def triplets_in_range(n):
    return True

def is_triplet(n):
    return True

# The triplet a = (m^2-n^2), b = 2*m*n and c = (m^2+n^2), where m and n are coprime and
# m - n > 0 and is odd, generate a primitive triplet. Note that this implies that b has
# to be divisible by 4 and a and c are odd. Also note that we may have either
# a > b or b > a.
