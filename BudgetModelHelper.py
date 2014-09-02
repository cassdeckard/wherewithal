from Ledger import Ledger
from Transaction import Transaction
from DataModel import DataModel
from DataModelAdapter import DataModelAdapter

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

def get_model() :
    model = DataModel()

    try :
        with open(DATA_FILE, 'rb') as infile :
            model.root = pickle.load(infile)
    except :
        print("Load from '%s' failed, falling back to test data..." %DATA_FILE)
        model.root = getTestDataModel()

    model.setHeaders(list(model.root.keys()))
    return model
