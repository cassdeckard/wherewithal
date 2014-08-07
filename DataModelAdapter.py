from PySide import QtCore

class DataModelAdapter(QtCore.QAbstractItemModel) :

    def __init__(self, data) :
        super(DataModelAdapter, self).__init__(None)
        self._data = data

    def columnCount(self, parent) :
        if len(self._data) :
            return len(self._data[0].keys())
        return 0

    def rowCount(self, parent) :
        return 0
