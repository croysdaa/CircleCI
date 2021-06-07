import example
import unittest


class TestCase (unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)
    def test_sub_1(self):
        self.assertEqual(example.sub(3, 2), 1)


if __name__ == '__main__':
    unittest.main()
