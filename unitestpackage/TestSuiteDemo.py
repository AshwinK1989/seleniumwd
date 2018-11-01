import unittest
from unitestpackage.AssertDemo import AssertDemo
from unitestpackage.UnitTestDemo import UnitTestDemo

tc1 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(smoke_test)
