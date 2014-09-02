from Transaction import Transaction
from DataModelAdapter import DataModelAdapter

from PySide.QtGui import *
from PySide.QtCore import *

class BudgetTreeView(QTreeView) :
    def __init__(self, model) :
        super(BudgetTreeView, self).__init__()

        self.setModel(model)
        self.initUI()

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
        new_data_model = DataModelAdapter(Transaction())
        self.model().addItem(new_data_model)
