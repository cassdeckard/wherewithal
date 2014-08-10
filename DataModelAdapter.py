
class DataModelAdapter(object) :

    def __init__(self, data) :
        self._data = data
        self._children = set()
        pass

    def numChildren(self) :
        return len(self._children)

    def hasData(self) :
        return True

    def getData(self, key) :
        return self._data[key]

    def addChild(self, child) :
        self._children.add(child)
