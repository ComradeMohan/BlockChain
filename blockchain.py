import hashlib
import time
import json
from typing import List

# 1. Block Structure
class Block:
    def __init__(self, index: int, transactions: List[str], timestamp: float, previous_hash: str):
        """Initialize a block with required attributes."""
        self.index = index                  # Block number
        self.transactions = transactions    # List of transactions
        self.timestamp = timestamp          # Creation timestamp
        self.previous_hash = previous_hash  # Previous block's hash
        self.nonce = 0                      # For proof-of-work
        self.hash = None                    # Current hash, set after mining

    def compute_hash(self) -> str:
        """Compute SHA-256 hash of block data."""
        block_data = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()

# 3. Blockchain Class
class Blockchain:
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Block] = []
        self.difficulty = 3  # Proof-of-work requires 3 leading zeros
        self._print_step("=== Blockchain Simulation Begins ===")
        self._print_step("Step 1: Creating Genesis Block...")
        self._create_genesis_block()

    def _print_step(self, message: str):
        """Print simulation steps with a delay for effect."""
        print(f"\n{message}")
        time.sleep(0.5)  # Short delay to simulate processing

    def _create_genesis_block(self):
        """Create the first block."""
        genesis = Block(0, ["Genesis: Blockchain started"], time.time(), "0")
        self._mine_block(genesis)
        self.chain.append(genesis)
        self._print_step(f"Genesis Block mined - Hash: {genesis.hash}")

    def _mine_block(self, block: Block):
        """Mine a block using proof-of-work."""
        self._print_step(f"Step: Mining Block {block.index} (target: '000'... hash)")
        start_time = time.time()
        block.hash = block.compute_hash()
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        end_time = time.time()
        self._print_step(f"Block {block.index} mined! Nonce: {block.nonce}, Time: {end_time - start_time:.2f}s")

    def add_block(self, transactions: List[str] = None):
        """Add a block, either with provided transactions or inline input."""
        if transactions is None:
            self._print_step("Step: Enter transactions for the new block (one per line, empty line to finish):")
            transactions = []
            while True:
                tx = input("> ").strip()
                if not tx:
                    break
                transactions.append(tx)
            if not transactions:
                transactions = ["Default: No transactions provided"]
        index = len(self.chain)
        self._print_step(f"Step: Adding Block {index} with transactions: {transactions}")
        previous_hash = self.chain[-1].hash
        new_block = Block(index, transactions, time.time(), previous_hash)
        self._mine_block(new_block)
        self.chain.append(new_block)
        self._print_step(f"Block {index} added to the chain!")

    def validate_chain(self) -> bool:
        """Check the chain's integrity."""
        self._print_step("Step: Validating the blockchain...")
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.compute_hash():
                self._print_step(f"Validation failed: Block {i} hash is invalid!")
                return False
            if current.previous_hash != previous.hash:
                self._print_step(f"Validation failed: Block {i} previous hash mismatch!")
                return False
        self._print_step("Blockchain is valid!")
        return True

    def print_chain(self):
        """Display all blocks in the chain."""
        self._print_step("Step: Displaying the blockchain...")
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {time.ctime(block.timestamp)}")
            print(f"  Transactions: {block.transactions}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Current Hash: {block.hash}")
            print(f"  Nonce: {block.nonce}")
            print()

# Simulation with inline input and automated demo
def run_simulation():
    blockchain = Blockchain()

    # Automated demo blocks
    blockchain.add_block(["Alice sends 10 BTC to Bob"])
    blockchain.add_block(["Bob sends 5 BTC to Charlie"])

    # Interactive block with inline input
    blockchain._print_step("Now, you can add a custom block! (Press Enter twice to use default)")
    blockchain.add_block()

    # Show and validate the chain
    blockchain.print_chain()
    blockchain.validate_chain()

    # Tampering demonstration
    blockchain._print_step("Step: Tampering with Block 1 for demonstration...")
    blockchain.chain[1].transactions = ["Hacker steals 1000 BTC"]
    blockchain._print_step("Block 1 tampered! New transactions: " + str(blockchain.chain[1].transactions))
    blockchain.print_chain()
    blockchain.validate_chain()

    blockchain._print_step("=== Blockchain Simulation Complete ===")

if __name__ == "__main__":
    run_simulation()