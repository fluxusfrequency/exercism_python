def smallest_palindrome(max_factor, min_factor = 0):
    return (9, set({1, 9}))

def largest_palindrome(max_factor, min_factor = 0):
    largest = 0
    factors = list()
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if (_is_palindrome(product)):
                if largest < product:
                    largest = product
                if ((i, j) not in factors):
                    factors.append((i, j))
    return (largest, factors)

def _is_palindrome(number):
    num = str(number)
    if (num == num[::-1]):
        return True
    return False
