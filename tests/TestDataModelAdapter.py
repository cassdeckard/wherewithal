import DataModelAdapter

import unittest

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

    def test_addChild_sets_parent_of_child_to_self(self) :
        child = DataModelAdapter.DataModelAdapter(None)
        self.assertIsNone(child.parent())
        self.test_object.addChild(child)
        self.assertIs(child.parent(), self.test_object)
