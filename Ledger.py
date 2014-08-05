
class Ledger(object) :
    def __init__(self) :
        self._list = []
        pass

    def add_transaction(self, transaction) :
        self._list.append({})
        pass

    def __delitem__(self, key) :
        self._list.__delitem__(key)

    def __getitem__(self, key) :
        return self._list.__getitem__(key)

    def __setitem__(self, key) :
        self._list.__setitem__(key)
