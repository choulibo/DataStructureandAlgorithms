#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 09_bubble_sort.py

def Bubble_sort(alist):
    """冒泡排序"""
#
#     for j in range(len(alist)-1,0,-1):
#         # j表示每次遍历需要比较的次数，逐渐减少的
#         for i in range(j):
#             if alist[i] > alist[i+1]:
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-1-j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

li = [54,26,93,17,77,31,44,55,20]
print(li)
Bubble_sort(li)
print(li)