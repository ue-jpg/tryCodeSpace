#!/usr/bin/env python3
import unittest
from hello import greet, add_numbers

class TestHelloFunctions(unittest.TestCase):
    
    def test_greet(self):
        """greet関数のテスト"""
        result = greet("テスト")
        self.assertEqual(result, "こんにちは、テストさん！")
    
    def test_add_numbers(self):
        """add_numbers関数のテスト"""
        # 正の数のテスト
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(10, 20), 30)
        
        # 負の数のテスト
        self.assertEqual(add_numbers(-5, 3), -2)
        self.assertEqual(add_numbers(-10, -5), -15)
        
        # 小数のテスト
        self.assertAlmostEqual(add_numbers(1.5, 2.3), 3.8)

if __name__ == "__main__":
    unittest.main()
