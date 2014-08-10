#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore
from Ledger import Ledger
from Transaction import Transaction
from DataModelAdapter import DataModelAdapter

class DataItem(object) :
   def __init__(self, data, parent=None) :
      self._data = data
      self.parent = parent
      self.children = []

   def addChild(self, childData) :
      child = DataItem(childData, self)
      self.children.append(child)
      return child

   def numChildren(self) :
      return len(self.children)

   def child(self, row) :
      return self.children[row]

   def row(self) :
      if self.parent :
         return self.parent.children.index(self)
      return 0

   def hasData(self) :
      return self._data is not None

   def numData(self) :
      return len(self._data)

   def getData(self, index) :
      return self._data[index]

   def setData(self, index, value) :
      self._data[index] = value

   def __repr__(self) :
      return "<%s object at %s, _data: %s, %s children>" %(
            self.__class__.__name__,
            hex(id(self)),
            self._data,
            self.numChildren())

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
      return item.getData(key)

   def headerData(self, section, orientation, role) :
      if (orientation == QtCore.Qt.Horizontal
              and role == QtCore.Qt.DisplayRole) :
         return self._headers

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
      item.setData(index.column(), value)
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
        t['header1'] = 'do'
        t['header2'] = 'a deer'
        #t['header3'] = '1'
        ledger.add_transaction(t)
        t = Transaction()
        t['header1'] = 're'
        t['header2'] = 'a drop of golden sun'
        t['header3'] = '2'
        ledger.add_transaction(t)

        self.setModel(DataModel())

        # root = DataItem(["header1", "header2", "header3"])
        self.model().root = DataModelAdapterMake(ledger)
        print(self.model().root)
        self.model().setHeaders(('header1', 'header2', 'header3'))
        # root.addChild(["do", "a deer, a female deer", "1"])
        # root.addChild(["re", "a drop of golden sun", "2"])
        # root.addChild(["mi", "a name I call myself", "3"])
        # c = root.addChild(["fa", "a long, long way to run", "4"])
        # c.addChild(["fafafafa", "test", "cinco"])

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
