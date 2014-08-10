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

    def test_hasData_returns_True(self) :
        self.assertTrue(self.test_object.hasData())

    def test_numChildren_returns_length_of_data(self) :
        self.test_data['foo'] = 1
        self.assertEqual(self.test_object.numChildren(), 1)

    def test_getData_returns_data_for_given_key(self) :
        key = 'bar'
        expected = 'hello'
        self.test_data[key] = expected
        self.assertEqual(self.test_object.getData(key), expected)
