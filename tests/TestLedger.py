import Ledger
from Transaction import Transaction

import unittest

class TestLedger(unittest.TestCase) :

    def setUp(self) :
        self.test_object = Ledger.Ledger()

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

    def test_add_transaction(self) :
        transaction = Transaction()
        self.test_object.add_transaction(transaction)
        self.assertIn(transaction, self.test_object)

    def test_different_transaction_is_not_in_ledger(self) :
        transaction1 = Transaction()
        transaction2 = Transaction()
        self.test_object.add_transaction(transaction1)
        self.assertNotIn(transaction2, self.test_object)

    def test_len(self) :
        self.assertEqual(len(self.test_object), 0)
        self.test_object.add_transaction(Transaction())
        self.assertEqual(len(self.test_object), 1)
        self.test_object.add_transaction(Transaction())
        self.assertEqual(len(self.test_object), 2)
