from PySide.QtGui import *
from PySide.QtCore import *

from Ledger import Ledger

class DataModel(QAbstractItemModel) :
    def __init__(self, ledger, parent=None) :
        super(DataModel, self).__init__(parent)
        self._ledger = ledger
        self._headers = list(ledger.keys())

    # QAbstractItemModel methods

    def columnCount(self, parent) :
        return len(self._headers)

    def rowCount(self, parent) :
        if parent.isValid() :
            return 0
            # TODO: support subtrees
        return len(self._ledger)

    def data(self, index, role) :
        if not index.isValid() :
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole :
            return str(index.internalPointer())

        return None

    def headerData(self, section, orientation, role) :
        if (orientation == Qt.Horizontal
                  and role == Qt.DisplayRole) :
            return self._headers[section]

        return None

    def index(self, row, column, parent) :
        if not self.hasIndex(row, column, parent) :
            return QModelIndex()

        # TODO: support subtrees
        transaction = self._ledger[row]
        key = self._headers[column]
        data = transaction[key] if key in transaction else None
        return self.createIndex(row, column, data)

    def parent(self, index) :
        if not index.isValid() :
            return QModelIndex()

        # TODO: support subtrees
        return QModelIndex()

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

        transaction = self._ledger[index.row()]
        # TODO: support subtrees

        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        key = self._headers[index.column()]
        transaction[key] = value
        self.emit(SIGNAL("layoutChanged()"))
        return True

    # Public methods

    def setHeaders(self, headers) :
        self._headers = headers

    def addHeader(self, header) :
        self._headers.append(header)

    def addItem(self, item):
        numRows = len(self._ledger)
        self.beginInsertRows(QModelIndex(), numRows, numRows)
        self._ledger.add_transaction(item)
        self.endInsertRows()
