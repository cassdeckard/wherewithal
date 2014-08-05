import DataModelAdapter
from PySide import QtCore

import unittest

class TestDataModelAdapter(unittest.TestCase) :

    def setUp(self) :
        self.test_data = {}
        self.test_object = DataModelAdapter.DataModelAdapter(self.test_data)

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

    def test_inherits_QAbstractItemModel(self) :
        self.assertIsInstance(self.test_object, QtCore.QAbstractItemModel)

    def test_after_init_parent_is_none(self) :
        self.assertIsNone(self.test_object.parent())

    def test_data(self) :
        self.test_object.data()
