import Transaction

import unittest

class TestTransaction(unittest.TestCase) :

    def setUp(self) :
        self.test_object = Transaction.Transaction()

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

    def test_can_assign_data(self) :
        self.test_object['foo'] = 'bar'
        self.assertIn('foo', self.test_object)
        self.assertEqual(self.test_object['foo'], 'bar')
