from blockchain import Blockchain
from data import transactions


if __name__ == "__main__":
    blockchain = Blockchain()
    for i in range(30):
        blockchain.add_block(transactions[i])
    blockchain.print_blocks()
    print(f'Blockchain validation: {blockchain.validate()}')