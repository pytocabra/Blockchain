from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block({}, 0)
        self.chain.append(genesis)
        return self.chain

    def print_blocks(self):
        for block in self.chain:
            print(f'Block no. {self.chain.index(block)}')
            print(block)

    def add_block(self, transactions):
        previous_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)

b = Blockchain()
b.add_block({'fsdf':1})
b.print_blocks()