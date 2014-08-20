
class Transaction(object) :
    def __init__(self) :
        self._dict = {}

    def __getitem__(self, key) :
        return self._dict.__getitem__(key)

    def __setitem__(self, key, value) :
        self._dict.__setitem__(key, value)

    def __contains__(self, key) :
        return self._dict.__contains__(key)
