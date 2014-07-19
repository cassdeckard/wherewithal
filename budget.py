#!/usr/bin/env python

import sys
from PySide import QtGui, QtCore

class DataItem(object) :
   def __init__(self, data, parent=None) :
      self.data = data
      self.parent = parent
      self.children = []

   def addChild(self, childData) :
      child = DataItem(childData, self)
      self.children.append(child)

   def numChildren(self) :
      return len(self.children)

   def child(self, row) :
      return self.children[row]

class DataModel(QtCore.QAbstractItemModel) :
   def __init__(self, parent=None) :
      super(DataModel, self).__init__(parent)
      self.root = None

   def columnCount(self, parent) :
      if not self.root :
         return 0
      if not self.root.data :
         return 0

      return len(self.root.data)

   def rowCount(self, parent) :
      if parent.isValid() :
         return 0
      return self.root.numChildren()

   def data(self, index, role) :
      if not index.isValid() :
         return None

      if role != QtCore.Qt.DisplayRole :
         return None

      item = index.internalPointer()
      return item.data[index.column()]

   def headerData(self, section, orientation, role) :
      if (orientation == QtCore.Qt.Horizontal
              and role == QtCore.Qt.DisplayRole) :
         return self.root.data[section]

      return None

   def index(self, row, column, parent) :
      if not self.hasIndex(row, column, parent) :
         return QtCore.QModelIndex()

      if not parent.isValid() :
         if (column < self.columnCount(parent)
                 and row < self.rowCount(parent)) :
            return self.createIndex(row, column, self.root.child(row))

   def parent(self, index) :
      if not index.isValid() :
         return QtCore.QModelIndex()
      return QtCore.QModelIndex()

   def flags(self, index) :
      if not index.isValid() :
         return QtCore.Qt.NoItemFlags

      return (QtCore.Qt.ItemIsEnabled
              | QtCore.Qt.ItemIsSelectable
              | QtCore.Qt.ItemIsEditable)

   def setData(self, index, value, role) :
      if role != QtCore.Qt.EditRole :
         print "setData: role is {}, not EditRole!".format(role)
         return False

      item = index.internalPointer()
      item.data[index.column()] = value
      return True

class MainApp(QtGui.QTreeView) :
    def __init__(self) :
        super(MainApp, self).__init__()

        self.initUI()

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')
        self.setModel(DataModel())
        root = DataItem(["header1", "header2", "header3"])
        self.model().root = root
        root.addChild(["do", "a deer, a female deer", "1"])
        root.addChild(["re", "a drop of golden sun", "2"])
        root.addChild(["mi", "a name I call myself", "3"])
        root.addChild(["fa", "a long, long way to run", "4"])

        self.show()

def main() :
    app = QtGui.QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
