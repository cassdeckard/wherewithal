#!/usr/bin/env python

import sys
from PySide import QtGui

class MainApp(QtGui.QWidget) :
    def __init__(self) :
        super(MainApp, self).__init__()

        self.initUI()

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')

        self.show()

def main() :
    app = QtGui.QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
