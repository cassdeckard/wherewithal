#!/usr/bin/env python

import sys
from PySide import QtGui, QtCore

class DataModel(QtCore.QAbstractItemModel) :
   def __init__(self, parent=None) :
      super(DataModel, self).__init__(parent)

   def columnCount(self, parent) :
      return 2

   def rowCount(self, parent) :
      if parent.isValid() :
         return 0
      return 3

   def data(self, index, role) :
      if not index.isValid() :
         return None

      if role != QtCore.Qt.DisplayRole :
         return None

      return "data @ {}".format(index)

   def headerData(self, section, orientation, role) :
      if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
         result = ("col_1", "col_2")[section]
         return result

      return None

   def index(self, row, column, parent) :
      if not self.hasIndex(row, column, parent) :
         return QtCore.QModelIndex()

      if not parent.isValid() :
         if column < 2 and row < 3 :
            return self.createIndex(row, column, "index @({}, {})".format(row, column))

   def parent(self, index) :
      if not index.isValid() :
         return QtCore.QModelIndex()
      return QtCore.QModelIndex()


class MainApp(QtGui.QTreeView) :
    def __init__(self) :
        super(MainApp, self).__init__()

        self.initUI()

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')
        self.setModel(DataModel())

        self.show()

def main() :
    app = QtGui.QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
