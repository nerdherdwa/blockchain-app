from scripts.modules.blockchain.block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        replace the local chain with the incoming one if the following applies:
         - the incoming chain is longer than the local one
         - the incoming chain is formatted correctly
        """
        if len(chain) <= len(self.chain):
            raise Exception('can not replace. the incoming chain must be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'can not replace. incoming chain is invalid: {e}')

        self.chain = chain

    @staticmethod
    def is_valid_chain(chain):
        """
        validate the incoming chain.
        Enforce the following rules of the blockchain:
         - the chain must start with the genesis block.
         - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('the genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
