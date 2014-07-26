#!/usr/bin/env python3

import Transaction

import unittest

class TestTransaction(unittest.TestCase) :

    def setUp(self) :
        pass

    def tearDown(self) :
        pass

    def test_init_Transaction(self) :
        t = Transaction.Transaction()
        self.assertIsNotNone(t)

if __name__ == '__main__' :
    unittest.main()
