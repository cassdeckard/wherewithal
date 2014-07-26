import Ledger

import unittest

class TestLedger(unittest.TestCase) :

    def setUp(self) :
        self.test_object = Ledger.Ledger()

    def tearDown(self) :
        pass

    def test_not_None(self) :
        self.assertIsNotNone(self.test_object)

