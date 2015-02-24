__author__ = 'constantinose'


def get_primes(limit):
    # Returns an unsorted set of primes up to the defined limit
    primes = set()  # Set avoids duplication
    num = 2  # Initialize as first known prime

    while num <= limit:
        for prime in primes:
            # If modulus of iterated num is divisible by
            # another calculated prime, exit for loop
            if num % prime == 0:
                break
        else:
            primes.add(num)
        num += 1

    return primes