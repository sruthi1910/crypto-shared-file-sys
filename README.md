# crypto-shared-file-sys
the filesystem will first break the files into 4 chunks. These 4 chunks will be individually encrypted. Each chunk will have a unique filename which will make it difficult to predict and find the specific file chunk. It will also create 2 parity file block which will be used as a redundancy method to retrieve file content when some of them have been deleted.  We will also create Merkle tree and save the root in MongoDB which will be used to prove the authenticity and integrity of the file.
 
While recreating the file. We will open chunks one by one and decrypt them using the algorithm. The system will check whether files are accessible or missing. If few files are missing, it will invoke erasure coding module and try to recreate the content while also informing the user that the file has been tampered. After decrypting and recreating missing chunks (if necessary), we again create a Merkle tree compare the Merkle root from the MongoDB. This will give the user the proof whether the file has been tampered or not.
Our filesystem will be mainly used for cold data and confidential data which is not frequently edited. This can be scaled to a decentralized file system using either IPFS or blockchain. In a decentralized network, the file system will distribute the chunks throughout the network and using our method, only the owner of the file will be able to access it.


FLOWCHART
![Untitled document](https://github.com/sruthi1910/crypto-shared-file-sys/assets/68804192/ea79605e-f409-4f97-be89-02d5b04b1414)


EXPECTED OUTPUT
![sharedcrypto](https://github.com/sruthi1910/crypto-shared-file-sys/assets/68804192/ab10fa84-8c17-4313-aa3a-67414276ff07)
