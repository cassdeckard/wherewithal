from Transaction import Transaction
from DataModel import DataModel
from DataModelAdapter import DataModelAdapter

from PySide.QtGui import *
from PySide.QtCore import *

class BudgetTreeView(QTreeView) :
    def __init__(self) :
        super(BudgetTreeView, self).__init__()

        self.setModel(DataModel())
        self.initUI()

    def initUI(self) :
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
