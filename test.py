#!/usr/bin/env python3

import Transaction

import unittest

class TestTransaction(unittest.TestCase) :

    def setUp(self) :
        self.t = Transaction.Transaction()

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.t)

if __name__ == '__main__' :
    unittest.main()
