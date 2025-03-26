# QuadB Tech Blockchain Simulation 🔗🧊

## 📘 Project Overview

This is a comprehensive blockchain simulation implemented in Python, demonstrating core blockchain concepts including block creation, transaction management, proof-of-work mechanism, and chain integrity validation. The project was developed as part of the QuadB Tech Full Stack Developer challenge.

## ✨ Features

- 🧱 Customizable Block Structure
- 🔐 SHA-256 Cryptographic Hashing
- ⛏️ Proof-of-Work Mining Mechanism
- 📊 Transaction Management
- 🔍 Blockchain Integrity Validation
- 🖥️ Interactive Simulation Mode

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. Clone the Repository
```bash
git clone https://github.com/ComradeMohan/BlockChain.git
cd BlockChain
```

2. Create Virtual Environment
```bash
# On Windows
python -m venv blockchain_env
blockchain_env\Scripts\activate

# On macOS/Linux
python3 -m venv blockchain_env
source blockchain_env/bin/activate
```

3. Run the Simulation
```bash
python blockchain.py
```

## 🎮 Interactive Mode

The simulation offers an interactive mode where you can:
- Add custom transactions
- Mine blocks
- View blockchain details
- Validate blockchain integrity

### Menu Options
1. Add Transaction
2. Mine Pending Transactions
3. Print Blockchain
4. Validate Blockchain
5. Exit

## 🔬 Technical Details

### Core Components
- `Block` Class: Represents individual blocks in the chain
- `Blockchain` Class: Manages the entire blockchain ecosystem
- Proof-of-Work: Implements computational challenge for block mining
- SHA-256 Hashing: Ensures data integrity and chain linkage

### Proof-of-Work
- Difficulty level configurable
- Requires hash with specific number of leading zeros
- Prevents easy block creation and ensures network security

## 📊 Sample Output

```
=== Blockchain Simulation Begins ===

Step 1: Creating Genesis Block...

Step: Mining Block 0 (target: '000'... hash)

Block 0 mined! Nonce: 112, Time: 0.01s

Genesis Block mined - Hash: 00002ec62c0225e1fcc494480040a83b9b248045505e4909907a450f94d6263c

Step: Adding Block 1 with transactions: ['Alice sends 10 BTC to Bob']

Step: Mining Block 1 (target: '000'... hash)

Block 1 mined! Nonce: 220, Time: 0.00s

Block 1 added to the chain!

Step: Adding Block 2 with transactions: ['Bob sends 5 BTC to Charlie']

Step: Mining Block 2 (target: '000'... hash)

Block 2 mined! Nonce: 1222, Time: 0.01s

Block 2 added to the chain!
```

## 🧪 Testing

### Recommended Test Scenarios
- Add multiple transactions
- Mine blocks with different miners
- Attempt to tamper with blockchain
- Validate chain integrity

## 🔧 Customization

You can easily modify:
- Proof-of-work difficulty
- Transaction structure
- Mining rewards
- Hashing algorithm

## 📈 Potential Enhancements
- Persistent storage
- Network simulation
- Advanced consensus mechanisms
- More complex transaction validation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

Project Link: [https://github.com/ComradeMohan/BlockChain]( https://github.com/ComradeMohan/BlockChain)

QuadB Tech HR: hr@quadbtech.com

## 🙏 Acknowledgements
- Python Community
- Blockchain Developers Worldwide
- QuadB Technologies

---

**Note**: This is a simulation for educational purposes. Not intended for production cryptocurrency implementation.
