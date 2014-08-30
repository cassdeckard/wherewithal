#!/usr/bin/env python3

import sys
from PySide.QtGui import *
from PySide.QtCore import *

from Ledger import Ledger
from Transaction import Transaction
from DataModelAdapter import DataModelAdapter

class DataModel(QAbstractItemModel) :
    def __init__(self, parent=None) :
        super(DataModel, self).__init__(parent)
        self.root = None
        self._headers = ()

    def setHeaders(self, headers) :
        self._headers = headers

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

class MainApp(QWidget) :
    def __init__(self) :
        QWidget.__init__(self, parent=None)

        vbox = QVBoxLayout()
        budget_tree_view = BudgetTreeView()
        vbox.addWidget(budget_tree_view)

        button = QPushButton("Add transaction")
        button.clicked.connect(budget_tree_view.addTransaction)
        vbox.addWidget(button)

        button = QPushButton("Add header")
        button.clicked.connect(budget_tree_view.addHeader)
        vbox.addWidget(button)

        self.setLayout(vbox)

class BudgetTreeView(QTreeView) :
    def __init__(self) :
        super(BudgetTreeView, self).__init__()

        self.initUI()

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')

        self.setModel(DataModel())
        self.model().root = getTestDataModel()
        self.model().setHeaders(('Date', 'Amount', 'Payee'))

    @Slot()
    def addHeader(self) :
        text, ok = QInputDialog.getText(self, 'Add Header', 'Header name:')
        if ok:
            pass

    @Slot()
    def addTransaction(self) :
        self.model().addItem(Transaction())

def DataModelAdapterMake(ledger) :
    result = DataModelAdapter(None)
    for transaction in ledger :
        dma = DataModelAdapter(transaction)
        result.addChild(dma)
    return result

def getTestDataModel() :
    ledger = Ledger()

    t = Transaction()
    t['Date'] = 'today'
    t['Amount'] = 2394
    t['Payee'] = 'Schnucks'
    ledger.add_transaction(t)

    t = Transaction()
    t['Date'] = '11/5/1955'
    t['Amount'] = 10000
    t['Payee'] = 'Some guy'
    ledger.add_transaction(t)

    return DataModelAdapterMake(ledger)

def main() :
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
