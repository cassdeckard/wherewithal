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

    @staticmethod
    def appObjects() :
        app = QtGui.QApplication(sys.argv)
        mainApp = MainApp()
        return (app, mainApp)

def main() :
    (app, mainApp) = MainApp.appObjects()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
