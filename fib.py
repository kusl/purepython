# Fibonacci numbers module
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(fibonacci(9), 34)


if __name__ == '__main__':
    unittest.main()


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
