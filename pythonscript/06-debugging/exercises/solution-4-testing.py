#!/usr/bin/env python3
"""
Solution: Exercise 4 - Unit Testing
"""
import unittest

print("=" * 60)
print("Solution: Exercise 4 - Unit Testing")
print("=" * 60)

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)

print("\n✅ Solution completed!")
