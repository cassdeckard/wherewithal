
class DataModelAdapter(object) :

    def __init__(self, data) :
        self._data = data
        self._children = set()
        self._parent = None
        pass

    def numChildren(self) :
        return len(self._children)

    def hasData(self) :
        return self._data is not None

    def getData(self, key) :
        return self._data[key]

    def addChild(self, child) :
        self._children.add(child)

    def setParent(self, parent) :
        self._parent = parent

    def parent(self) :
        return self._parent
