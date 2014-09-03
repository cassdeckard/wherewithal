from DataModel import DataModel
from DataModelAdapter import DataModelAdapter
from Ledger import Ledger

import pickle

DATA_FILE='ledger.pickle'

def get_ledger() :
    result = None
    try:
        with open(DATA_FILE, 'rb') as infile:
            result = pickle.load(infile)
    except FileNotFoundError:
        pass
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass

    if not result: result = Ledger()
    return result

def get_model() :
    model = DataModel()

    model.setHeaders(list(model.root.keys()))
    return model

def save_ledger(ledger) :
    with open(DATA_FILE, 'wb') as outfile:
        pickle.dump(ledger, outfile, pickle.HIGHEST_PROTOCOL)
