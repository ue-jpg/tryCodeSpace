#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet(name):
    """挨拶を返す関数"""
    return f"こんにちは、{name}さん！"

def add_numbers(a, b):
    """2つの数値を足し算する関数"""
    return a + b

def main():
    # 基本的な挨拶
    print(greet("世界"))
    
    # 計算のテスト
    result = add_numbers(10, 25)
    print(f"10 + 25 = {result}")
    
    # ユーザー入力のテスト
    name = input("あなたの名前を入力してください: ")
    print(greet(name))

if __name__ == "__main__":
    main()
