from datetime import datetime  
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        # each block of blockchain contains: 
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def __repr__(self):
        result = f'Timestamp: {self.timestamp}\n'
        result += f'Transactions: {self.transactions}\n'
        result += f'Current hash: {self.generate_hash()}\n'
        result += f'Previous hash: {self.previous_hash}\n'
        return result

    def generate_hash(self):
        # generate_hash - generates block hash value using sha256 hash algorithm
        block_content = str(self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)
        hash_value = sha256(block_content.encode()) 
        return hash_value.hexdigest()