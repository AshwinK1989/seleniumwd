import unittest


class AssertDemo(unittest.TestCase):

    def test_assertEquals(self):

        a='ashwin'
        b='ashwin'
        self.assertEqual(a, b, 'Values are not equal')

    def test_assertTrue(self):

        self.assertTrue(False, 'The value is not true')


if __name__ == '__main__':
    unittest.main()

