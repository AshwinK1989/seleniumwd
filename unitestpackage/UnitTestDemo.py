import unittest


class UnitTestDemo(unittest.TestCase):

    def setUp(self):
        print('This will run before every Test')

    def test_method_A(self):
        print('Running the Method A')

    def test_method_B(self):
        print('Running the Method B')

    def tearDown(self):
        print('This will run after every Test')


if __name__ == '__main__':
    unittest.main()
