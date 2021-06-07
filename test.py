import example
import unittest


class TestCase (unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.sub(3, 2), 1)

    def test_mult_1(self):
        self.assertEqual(example.mult(3, 2), 6)

    def test_div_1(self):
        self.assertEqual(example.div(3, 2), 1.5)


if __name__ == '__main__':
    unittest.main()
