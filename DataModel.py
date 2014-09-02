from DataModelAdapter import DataModelAdapter

from PySide.QtGui import *
from PySide.QtCore import *

class DataModel(QAbstractItemModel) :
    def __init__(self, parent=None) :
        super(DataModel, self).__init__(parent)
        self.root = None
        self._headers = ()

    def save(self) :
        with open(DATA_FILE, 'wb') as outfile:
            pickle.dump(self.root, outfile, pickle.HIGHEST_PROTOCOL)

    def setHeaders(self, headers) :
        self._headers = headers

    def addHeader(self, header) :
        self._headers.append(header)

    def columnCount(self, parent) :
        return len(self._headers)

    def rowCount(self, parent) :
        if parent.isValid() :
            return parent.internalPointer().numChildren()
        return self.root.numChildren()

    def data(self, index, role) :
        if not index.isValid() :
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole :
            item = index.internalPointer()
            key = self._headers[index.column()]
            return str(item.getData(key))

        return None

    def headerData(self, section, orientation, role) :
        if (orientation == Qt.Horizontal
                  and role == Qt.DisplayRole) :
            return self._headers[section]

        return None

    def index(self, row, column, parent) :
        if not self.hasIndex(row, column, parent) :
            return QModelIndex()

        parentItem = self.root
        if parent.isValid() :
            parentItem = parent.internalPointer()
        if (column < self.columnCount(parent)
                  and row < self.rowCount(parent)) :
            return self.createIndex(row, column, parentItem.child(row))

    def parent(self, index) :
        if not index.isValid() :
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.root :
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def flags(self, index) :
        if not index.isValid() :
            return Qt.NoItemFlags

        return (Qt.ItemIsEnabled
                  | Qt.ItemIsSelectable
                  | Qt.ItemIsEditable)

    def setData(self, index, value, role) :
        if role != Qt.EditRole :
            print("setData: role is {}, not EditRole!".format(role))
            return False

        item = index.internalPointer()
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        item.setData(self._headers[index.column()], value)
        self.emit(SIGNAL("layoutChanged()"))
        return True

    def addItem(self, item):
        numRows = self.root.numChildren()
        self.beginInsertRows(QModelIndex(), numRows, numRows)
        self.root.addChild(DataModelAdapter(item))
        self.endInsertRows()
