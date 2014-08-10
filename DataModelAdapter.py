
class DataModelAdapter(object) :

    def __init__(self, data) :
        self._data = data
        pass

    def numChildren(self) :
        return 0

    def hasData(self) :
        return True

    def numData(self) :
        return len(self._data)

    def getData(self, key) :
        return self._data[key]
