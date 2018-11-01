import unittest
from unitestpackage.AssertDemo import AssertDemo
from unitestpackage.UnitTestDemo import UnitTestDemo

# First load the Test Case Classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo)

# Create a Test Suite
smoke_test = unittest.TestSuite([tc1, tc2])

# Run the Suite
unittest.TextTestRunner().run(smoke_test)
