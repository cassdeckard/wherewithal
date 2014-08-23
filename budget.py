#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore

from Ledger import Ledger
from Transaction import Transaction
from DataModelAdapter import DataModelAdapter

SIGNAL = QtCore.SIGNAL

class DataModel(QtCore.QAbstractItemModel) :
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

      if role != QtCore.Qt.DisplayRole :
         return None

      item = index.internalPointer()
      key = self._headers[index.column()]
      return str(item.getData(key))

   def headerData(self, section, orientation, role) :
      if (orientation == QtCore.Qt.Horizontal
              and role == QtCore.Qt.DisplayRole) :
         return self._headers[section]

      return None

   def index(self, row, column, parent) :
      if not self.hasIndex(row, column, parent) :
         return QtCore.QModelIndex()

      parentItem = self.root
      if parent.isValid() :
         parentItem = parent.internalPointer()
      if (column < self.columnCount(parent)
              and row < self.rowCount(parent)) :
         return self.createIndex(row, column, parentItem.child(row))

   def parent(self, index) :
      if not index.isValid() :
         return QtCore.QModelIndex()

      childItem = index.internalPointer()
      parentItem = childItem.parent()

      if parentItem == self.root :
         return QtCore.QModelIndex()

      return self.createIndex(parentItem.row(), 0, parentItem)

   def flags(self, index) :
      if not index.isValid() :
         return QtCore.Qt.NoItemFlags

      return (QtCore.Qt.ItemIsEnabled
              | QtCore.Qt.ItemIsSelectable
              | QtCore.Qt.ItemIsEditable)

   def setData(self, index, value, role) :
      if role != QtCore.Qt.EditRole :
         print("setData: role is {}, not EditRole!".format(role))
         return False

      item = index.internalPointer()
      self.emit(SIGNAL("layoutAboutToBeChanged()"))
      item.setData(self._headers[index.column()], value)
      self.emit(SIGNAL("layoutChanged()"))
      return True

class MainApp(QtGui.QTreeView) :
    def __init__(self) :
        super(MainApp, self).__init__()

        self.initUI()

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')

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

        self.setModel(DataModel())
        self.model().root = DataModelAdapterMake(ledger)
        self.model().setHeaders(('Date', 'Amount', 'Payee'))

        self.show()

def DataModelAdapterMake(ledger) :
    result = DataModelAdapter(None)
    for transaction in ledger :
        dma = DataModelAdapter(transaction)
        result.addChild(dma)
    return result

def main() :
    app = QtGui.QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
