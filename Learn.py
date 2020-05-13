#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 16:14
# @Author  : lary
# @File    : Learn.py
# print('hello world',type('hello world'))
# print(1.0,type(1.0))
# print(2+3,type(2+3))
# a=10
# b=20
# if b>a:
#     print('123')
# else:
#     print('456')
# print('hello world')
# print(2+3)
# a=10
# print(a)
# b=8
# print(b)
# print(type(1))
# print(type(1.2))
# print(type("hello world"))
# print(isinstance(123,int))
# print(isinstance(1.2,float))
# print(isinstance('123',str))
# print(0b101001) #二进制
# print(0o101011) #十进制
# print(0x101011) #十六进制
#
# print(123==123.0)
# def add(a,b):
#     c=a+b
#     return c
# c=add(4,5)
# print(c)
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
print(my_abs(99))
print(my_abs(-99))