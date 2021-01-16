from random import choice, randint 
import string


def generate_random_name(length):
    # generates random name for sender and receiver in transactions
    symbols = string.hexdigits
    result = ''.join((choice(symbols)) for _ in range(length))
    return result


# generate random 30 transactions
transactions = [{'sender': generate_random_name(randint(5,9)), 'value': randint(1,300), 
                        'receiver': generate_random_name(randint(5,9))} for _ in range(30)]
