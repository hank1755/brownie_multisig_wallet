// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

/*
Verify signature takes 4 steps
1. message to sign | python web3.py create message to sign 
2. hash the message | python web3.py hash(message)
3. sign the hash of the message | python web3.py sign(hash(mssage), privatekey) - Ths is done offchain
4. ecrecover(hash(message), signature) == signer
*/

contract VerifySignature {
    function VerifyMessage(
        bytes32 _hashedMessage,
        uint8 _v,
        bytes32 _r,
        bytes32 _s
    ) public pure returns (address) {
        bytes memory prefix = "\x19Ethereum Signed Message:\n32";
        bytes32 prefixedHashMessage = keccak256(
            abi.encodePacked(prefix, _hashedMessage)
        );
        address signer = ecrecover(prefixedHashMessage, _v, _r, _s);
        return signer;
    }
}
