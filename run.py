from blockchain import Blockchain
from random import choice, randint 
import string


def generate_random_name(length):
    symbols = string.hexdigits
    result = ''.join((choice(symbols)) for _ in range(length))
    return result


# generate random 30 transactions
transactions = [{'sender': generate_random_name(randint(5,9)), 'value': randint(1,300), 
                        'receiver': generate_random_name(randint(5,9))} for _ in range(30)]



# create blockchain, add 30 blocks and validate
blockchain = Blockchain()

for i in range(30):
    blockchain.add_block(transactions[i])

blockchain.print_blocks()
print(f'Blockchain validation: {blockchain.validate()}')