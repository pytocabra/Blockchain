from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # create first block in chain
        genesis = Block({}, 0)
        self.chain.append(genesis)
        return self.chain

    def print_blocks(self):
        # print all blocks in chain
        for block in self.chain:
            print(f'Block no. {self.chain.index(block)}')
            print(block)

    def add_block(self, transactions):
        # add new block (transaction) to chain with proof of work
        previous_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return (proof, new_block)

    def validate(self):
        # validate chain integrity by checking previous hash values
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i-1]
            current_block = self.chain[i]
            if current_block.hash != current_block.generate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            return True

    def proof_of_work(self, block, proof_level=3):
        # calculate proof of work - last :proof_level 'zeros'
        proof = block.generate_hash()
        while proof[:proof_level] != '0' * proof_level:
            block.nonce += 1 
            proof = block.generate_hash()
        block.nonce = 0
        return proof

