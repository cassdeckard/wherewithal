import DataModelAdapter
from PySide import QtCore

import unittest

class TestDataModelAdapter(unittest.TestCase) :

    def setUp(self) :
        self.test_data = []
        self.test_object = DataModelAdapter.DataModelAdapter(self.test_data)

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

    def test_inherits_QAbstractItemModel(self) :
        self.assertIsInstance(self.test_object, QtCore.QAbstractItemModel)

    def test_after_init_parent_is_none(self) :
        self.assertIsNone(self.test_object.parent())

    def test_columnCount_returns_0_with_empty_data(self) :
        self.assertEqual(self.test_object.columnCount(None), 0)

    def test_rowCount_returns_0_with_empty_data(self) :
        self.assertEqual(self.test_object.rowCount(None), 0)

    def test_columnCount_returns_number_of_unique_keys_in_dictionaries(self) :
        self.test_data.append({'foo' : 'bar'})
        self.assertEqual(self.test_object.columnCount(None), 1)
        self.test_data.append({'foo' : 'baz'})
        self.assertEqual(self.test_object.columnCount(None), 1)
        self.test_data.append({'name' : 'Larry',
                               'foo'  : 'bar',
                              })
        self.assertEqual(self.test_object.columnCount(None), 2)

    def test_rowCount_returns_length_of_data(self) :
        self.test_data.append({'name' : 'Larry',
                               'foo'  : 'bar',
                              })
        self.assertEqual(self.test_object.rowCount(None), 1)
        self.test_data.append({});
        self.assertEqual(self.test_object.rowCount(None), 2)
        self.test_data.append({'foo' : 'baz'})
        self.assertEqual(self.test_object.rowCount(None), 3)

    def test_index_returns_QModelIndex(self) :
        result = self.test_object.index(0, 0, QtCore.QModelIndex())
        self.assertIsInstance(result, QtCore.QModelIndex)
