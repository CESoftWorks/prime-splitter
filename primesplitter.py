__author__ = 'constantinose'

import primesgenerator
import argparse
from collections import Counter


def main():
    # Parser to handle command line input
    input_parser = argparse.ArgumentParser(
        description="Program that splits an input number into its prime factors")
    input_parser.add_argument('number', nargs=1, type=int,
                              help="Number that is to be factorised")

    args = input_parser.parse_args()
    number = args.number[0]

    primes = primesgenerator.get_primes(number)

    # Bit of input checking
    if number in primes:
        print(str(number) +
              " is a prime, and thus cannot be factorised")
        return
    elif number is 1:
        print("1 is a very special number! Very special. Number.")
        return
    elif number < 1:
        print("Please enter a positive non-zero integer")
        return

    factors = []

    # Factorise
    for prime in primes:
        while number % prime == 0:
            factors.append(prime)
            number //= prime

    output = []
    # Count occurrences of the same primes
    # Counter(factors) returns a dictionary, which is then translated
    # to a list in order to make the output in the form of '2^2 x 3^2'
    for key, value in Counter(factors).items():
        if value != 1:
            # Do not use power notation for powers of 1
            output.append(str(key) + '^' + str(value))
        else:
            output.append(str(key))

    # Unpack output list elements and separate them by ' x ' sign
    print(*output, sep=' x ')


main()