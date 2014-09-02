from DataModel import DataModel
from DataModelAdapter import DataModelAdapter

import pickle

DATA_FILE='wherewithal.pickle'

def get_model() :
    model = DataModel()

    try :
        with open(DATA_FILE, 'rb') as infile :
            model.root = pickle.load(infile)
    except :
        model.root = DataModelAdapter(None)

    model.setHeaders(list(model.root.keys()))
    return model

def save_model(model) :
    with open(DATA_FILE, 'wb') as outfile:
        pickle.dump(model.root, outfile, pickle.HIGHEST_PROTOCOL)
