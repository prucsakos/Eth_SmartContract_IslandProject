const fs = require('fs');
const { MerkleTree } = require('merkletreejs');
const keccak256 = require('keccak256');

// Path of the addresses
const ADDRESSES_FILE_PATH = './test_addresses/addresses4000';

// Process the addresses. Read them into a list.
const data = fs.readFileSync(ADDRESSES_FILE_PATH, 'utf-8');
let whitelistAddresses = data.trim().split('\n').map(x => x.trim());

// Create leaf nodes by hashing every address. Then create the tree.
const leafNodes = whitelistAddresses.map(addr => keccak256(addr));
const merkleTree = new MerkleTree(leafNodes, keccak256, { sortPairs: true });

// Get the root hash (and pass it to the Smart Contract).
const rootHash = merkleTree.getRoot();
console.log('RootHash\n', merkleTree.getRoot().toString('hex'))

//SERVER SIDE:
// Recieve an address, hash it and make a proof. Then return is to the client.
const claimAddr = whitelistAddresses[1];
const claimHashed = keccak256(claimAddr);
const hexProof = merkleTree.getHexProof(claimHashed);

console.log('hexProof\n', hexProof);