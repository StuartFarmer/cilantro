import pprint

class Transaction(object):
    def __init__(self, wallet, proof):
        self.wallet = wallet
        self.proof_system = proof
        self.payload = None

    def __str__(self):
        return pprint.pformat(self.payload)

    def build(self, *args):
        raise NotImplementedError

    def sign(self, *args):
        raise NotImplementedError

    def seal(self, *args):
        raise NotImplementedError