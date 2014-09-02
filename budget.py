#!/usr/bin/env python3

from Ledger import Ledger
from Transaction import Transaction
from DataModelAdapter import DataModelAdapter
from DataModel import DataModel

from PySide.QtGui import *
from PySide.QtCore import *

import pickle
import sys

DATA_FILE='wherewithal.pickle'

class MainApp(QWidget) :
    def __init__(self) :
        QWidget.__init__(self, parent=None)

        vbox = QVBoxLayout()
        budget_tree_view = BudgetTreeView()
        vbox.addWidget(budget_tree_view)

        vbox.addWidget(self.make_button('Add transaction', budget_tree_view.addTransaction))
        vbox.addWidget(self.make_button('Add header', budget_tree_view.addHeader))
        vbox.addWidget(self.make_button('Save', budget_tree_view.save))

        self.setLayout(vbox)

    def make_button(self, title, slot) :
        button = QPushButton(title)
        button.clicked.connect(slot)
        return button

class BudgetTreeView(QTreeView) :
    def __init__(self) :
        super(BudgetTreeView, self).__init__()

        self.init_model()
        self.initUI()

    def init_model(self) :
        self.setModel(DataModel())

        try :
            with open(DATA_FILE, 'rb') as infile :
                self.model().root = pickle.load(infile)
        except :
            print("Load from '%s' failed, falling back to test data..." %DATA_FILE)
            self.model().root = getTestDataModel()

        self.model().setHeaders(list(self.model().root.keys()))

    def initUI(self) :
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Budget')

    @Slot()
    def addHeader(self) :
        text, ok = QInputDialog.getText(self, 'Add Header', 'Header name:')
        if ok:
            self.model().addHeader(text)
            self.header().reset()

    @Slot()
    def addTransaction(self) :
        self.model().addItem(Transaction())

    @Slot()
    def save(self) :
        self.model().save()

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
