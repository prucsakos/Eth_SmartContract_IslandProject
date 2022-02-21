# Technical infos
The smart contract was built upon the ERC721A standard. The main functionality of this specific standars is to mint any amount of nfts close to the cost of only 1 mint.

The application has a whitelist function. Uploading thousands of privileged addresses to the blockchain is very costful. Instead, we use Merkle hash trees to validate whitelisted members. This is done by maintaining a web application where members can request for a "proof", which is a small array of hash values. To validate the addresses we only need the proof to be passed to the smart contract, as it can calculate the root hash from the proof itself. If the new root hash matches the one that was gives at deploying, then we surely know whether the address is on the whitelist or not.
