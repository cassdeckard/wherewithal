from PySide import QtCore

class DataModelAdapter(QtCore.QAbstractItemModel) :

    def __init__(self, data) :
        super(DataModelAdapter, self).__init__(None)
        pass

    def columnCount(self, parent) :
        return 0
