# Technical infos
The smart contract was built upon the ERC721A standard. The main functionality of this specific standard is to mint any amount of nfts close to the cost of only 1 mint.
Their git repo is at the following link: 
https://github.com/chiru-labs/ERC721A

The application has a whitelist function. Uploading thousands of privileged addresses to the blockchain is very costful. Instead, we use Merkle hash trees to validate whitelisted members. This is done by maintaining a web application where members can request for a "proof", which is a small array of hash values. To validate the addresses we only need the proof to be passed to the smart contract, as it can calculate the root hash from the proof itself. If the new root hash matches the one that was gives at deploying, then we surely know whether the address is on the whitelist or not.
The merklee tree solution was inspired by and article at the following link: https://medium.com/@ItsCuzzo/using-merkle-trees-for-nft-whitelists-523b58ada3f9
