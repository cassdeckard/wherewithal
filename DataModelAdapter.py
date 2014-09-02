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
        if key in self._data :
            return self._data[key]
        return None

    def setData(self, key, value) :
        self._data[key] = value

    def addChild(self, child) :
        child.setParent(self)
        self._children.add(child)

    def child(self, row) :
        sort_key=lambda child : child.sort_key()
        try:
            children_list = sorted(self._children, key=sort_key)
        except:
            children_list = sorted(self._children, key=lambda child: str(child._data))
        return children_list[row]

    def setParent(self, parent) :
        self._parent = parent

    def parent(self) :
        return self._parent

    def sort_key(self) :
        return self._data.sort_key()

    def keys(self) :
        my_keys = set(self._data.keys()) if self._data else set()
        all_sets = [set(child.keys()) for child in self._children]
        return my_keys.union(*all_sets)
