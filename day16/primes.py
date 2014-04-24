#note this is not a complete program but only here to talk about list compression and for loops

def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result

def primes_upto(n):
    """ Return a list of all prime numbers less than n using a list comprehension. """
    result = [num for num in range(2,n) if is_prime(num)]
    return result

