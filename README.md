# Blockchain <img src="block.png" width="45" height="45"/>
Simple blockchain implementation using sha256 hash method and proof of work.

## Block
Each block contains:
- timestamp
- transactions
- sender and receiver name
- nonce

## Blochchain
Blokckchain has all needed functionality to run a simple network. <br/>

Blockchain methods:
- add block
- validate chain
- proof of work

## Proof of work
Used proof of work algorithm is calculating hash value to start with default 3 leading zeros.
```python
def proof_of_work(self, block, proof_level=3):
        proof = block.generate_hash()
        while proof[:proof_level] != '0' * proof_level:
            block.nonce += 1 
            proof = block.generate_hash()
        block.nonce = 0
        return proof

```
