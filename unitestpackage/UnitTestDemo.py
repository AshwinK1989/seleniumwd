import unittest


class UnitTestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('This will run before all the tests')

    def setUp(self):
        print('This will run before every Test')

    def test_method_A(self):
        print('Running the Method A')

    def test_method_B(self):
        print('Running the Method B')

    def tearDown(self):
        print('This will run after every Test')

    @classmethod
    def tearDownClass(self):
        print('This will run after all Tests')


if __name__ == '__main__':
    unittest.main()
