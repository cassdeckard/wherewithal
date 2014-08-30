import Transaction

from datetime import date

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

    def test_different_transactions_are_not_each_other(self) :
        emptyTransaction = Transaction.Transaction()
        self.assertIsNot(self.test_object, emptyTransaction)

    def test_different_transactions_with_same_data_are_equal(self) :
        self.test_object['foo'] = 'bar'
        newTransaction = Transaction.Transaction()
        newTransaction['foo'] = 'bar'
        self.assertEqual(self.test_object, newTransaction)

    def test_transaction_is_itself(self) :
        self.assertIs(self.test_object, self.test_object)

    def test_different_transactions_with_same_data_are_equal(self) :
        self.test_object['foo'] = 'bar'
        newTransaction = Transaction.Transaction()
        newTransaction['foo'] = 'baz'
        self.assertNotEqual(self.test_object, newTransaction)

    def test_Date_is_always_a_date(self) :
        transaction = Transaction.Transaction()
        self.assertIsInstance(transaction['Date'], date)

    def test_Date_converts_string_to_date(self) :
        self.test_object['Date'] = "1955-11-05"
        self.assertEqual(self.test_object['Date'], date(1955, 11, 5))

    def test_sort_key_returns_Date_field(self) :
        self.test_object['Date'] = "1993-09-03"
        self.assertEqual(self.test_object.sort_key(), date(1993, 9, 3))

    def test_keys_returns_keys(self) :
        self.assertSetEqual(set(self.test_object.keys()), {'Date'})
        self.test_object['monty'] = None
        self.assertSetEqual(set(self.test_object.keys()), {'Date', 'monty'})
        self.test_object['python'] = 1
        self.assertSetEqual(set(self.test_object.keys()), {'Date', 'monty', 'python'})
