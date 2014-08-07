from PySide import QtCore

import itertools

class DataModelAdapter(QtCore.QAbstractItemModel) :

    def __init__(self, data) :
        super(DataModelAdapter, self).__init__(None)
        self._data = data

    def columnCount(self, parent) :
        all_keys = set(itertools.chain.from_iterable(
            [d.keys() for d in self._data])
        )
        return len(all_keys)

    def rowCount(self, parent) :
        return 0
