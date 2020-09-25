# -*- coding: utf-8 -*-
"""
建檔日期：2020 09 25 Fri

@作者: Devin

@標題: 數字輸入與計算練習

@說明: 輸入兩個數字, 顯示其加、減、乘、除、整除和餘數
"""

print("數字輸入與計算練習")
print("作者：Devin 2020.9.25")
print("---------------------")
a = int(input("請輸入第一個數字:"))
b = int(input("請輸入第二個數字:"))

print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '*', b, '=', a*b)
print(a, '/', b, '=', a/b)
print(a, '//', b, '=', a//b)
print(a, '%', b, '=', a%b)
