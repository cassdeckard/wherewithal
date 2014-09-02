from Ledger import Ledger
from Transaction import Transaction
from DataModel import DataModel
from DataModelAdapter import DataModelAdapter

from PySide.QtGui import *
from PySide.QtCore import *

import pickle

DATA_FILE='wherewithal.pickle'

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

def DataModelAdapterMake(ledger) :
    result = DataModelAdapter(None)
    for transaction in ledger :
        dma = DataModelAdapter(transaction)
        result.addChild(dma)
    return result

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

