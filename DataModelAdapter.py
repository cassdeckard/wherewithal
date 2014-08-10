
class DataModelAdapter(object) :

    def __init__(self, data) :
        self._data = data
        pass

    def numChildren(self) :
        return len(self._data)

    def hasData(self) :
        return True

    def getData(self, key) :
        return self._data[key]
