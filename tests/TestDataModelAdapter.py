import DataModelAdapter

from datetime import date

import unittest
from unittest.mock import MagicMock

def make_DataModelAdapter_with_sort_key(sort_key) :
    mockData = MagicMock()
    mockData.sort_key = MagicMock(return_value=sort_key)
    result = DataModelAdapter.DataModelAdapter(mockData)
    return result

def make_DataModelAdapter_with_str(string) :
    mockData = MagicMock()
    mockData.__str__.return_value = string
    result = DataModelAdapter.DataModelAdapter(mockData)
    return result

def make_test_object_with_keys(*args) :
    data = dict()
    for arg in args :
        data[arg] = None
    return DataModelAdapter.DataModelAdapter(data)

class TestDataModelAdapter(unittest.TestCase) :

    def setUp(self) :
        self.test_data = {}
        self.test_object = DataModelAdapter.DataModelAdapter(self.test_data)

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

    def test_numChildren_returns_0_when_data_is_empty(self) :
        result = self.test_object.numChildren()
        self.assertEqual(result, 0)

    def test_hasData_returns_False_if_data_is_None(self) :
        self.test_object = DataModelAdapter.DataModelAdapter(None)
        self.assertFalse(self.test_object.hasData())

    def test_hasData_returns_True_if_data_exists(self) :
        self.assertTrue(self.test_object.hasData())

    def test_numChildren_returns_length_of_children(self) :
        self.assertEqual(self.test_object.numChildren(), 0)
        child = DataModelAdapter.DataModelAdapter(None)
        self.test_object.addChild(child)
        self.assertEqual(self.test_object.numChildren(), 1)

    def test_getData_returns_None_if_data_is_None(self) :
        self.assertIsNone(self.test_object.getData('anything'))

    def test_getData_returns_None_if_key_does_not_exist(self) :
        self.test_data['key'] = 'value'
        self.assertIsNone(self.test_object.getData('nonexistent_key'))

    def test_getData_returns_data_for_given_key(self) :
        key = 'bar'
        expected = 'hello'
        self.test_data[key] = expected
        self.assertEqual(self.test_object.getData(key), expected)

    def test_setData_sets_data(self) :
        key = 'bar'
        expected = 'hello'
        self.test_data[key] = 'unexected'
        self.test_object.setData(key, expected)
        self.assertEqual(self.test_object.getData(key), expected)

    def test_addChild_sets_parent_of_child_to_self(self) :
        child = DataModelAdapter.DataModelAdapter(None)
        self.assertIsNone(child.parent())
        self.test_object.addChild(child)
        self.assertIs(child.parent(), self.test_object)

    def test_children_sorted_by_sort_key(self) :
        data0 = make_DataModelAdapter_with_sort_key(0)
        data1 = make_DataModelAdapter_with_sort_key(1)
        data2 = make_DataModelAdapter_with_sort_key(2)
        data3 = make_DataModelAdapter_with_sort_key(3)
        self.test_object.addChild(data0)
        self.test_object.addChild(data3)
        self.test_object.addChild(data1)
        self.test_object.addChild(data2)
        self.assertEqual(self.test_object.child(0), data0)
        self.assertEqual(self.test_object.child(1), data1)
        self.assertEqual(self.test_object.child(2), data2)
        self.assertEqual(self.test_object.child(3), data3)

    def test_children_sorted_by_string_repr_if_sort_key_undefined(self) :
        data0 = make_DataModelAdapter_with_str('a')
        data1 = make_DataModelAdapter_with_str('b')
        data2 = make_DataModelAdapter_with_str('bed')
        data3 = make_DataModelAdapter_with_str('c')
        self.test_object.addChild(data2)
        self.test_object.addChild(data0)
        self.test_object.addChild(data3)
        self.test_object.addChild(data1)
        self.assertEqual(self.test_object.child(0), data0)
        self.assertEqual(self.test_object.child(1), data1)
        self.assertEqual(self.test_object.child(2), data2)
        self.assertEqual(self.test_object.child(3), data3)

    def test_keys_returns_keys_of_all_children(self) :
        self.test_object.addChild(make_test_object_with_keys("a", "b", "c"))
        self.test_object.addChild(make_test_object_with_keys("foo", "bar", "c"))
        self.assertSetEqual(self.test_object.keys(), {"a", "b", "c", "foo", "bar"})
        self.test_object.addChild(make_test_object_with_keys("Larry", "foo", "Moe"))
        self.assertSetEqual(self.test_object.keys(), {"a", "b", "c", "foo", "bar", "Larry", "Moe"})
