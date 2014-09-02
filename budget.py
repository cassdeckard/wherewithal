#!/usr/bin/env python3

from BudgetTreeView import BudgetTreeView
from BudgetModelHelper import get_model, save_model

from PySide.QtGui import *
from PySide.QtCore import *

import sys

class MainApp(QWidget) :
    def __init__(self) :
        QWidget.__init__(self, parent=None)

        vbox = QVBoxLayout()
        budget_tree_view = BudgetTreeView(get_model())
        vbox.addWidget(budget_tree_view)

        vbox.addWidget(self.make_button('Add transaction', budget_tree_view.addTransaction))
        vbox.addWidget(self.make_button('Add header', budget_tree_view.addHeader))
        vbox.addWidget(self.make_button('Save', lambda: save_model(budget_tree_view.model())))

        self.setLayout(vbox)

    def make_button(self, title, slot) :
        button = QPushButton(title)
        button.clicked.connect(slot)
        return button

def main() :
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
