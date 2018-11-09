#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 10_select_sort.py

def select_sort(alist):
    """升序排列"""
    n = len(alist)
    for i in range(n-1):
        # 记录最小值,假定第一个值就是最小值
        min_index = i
        # 从i+1到末尾选择最小值
        for j in range(i+1,n):
            if alist(j) < alist(min_index):
                min_index = j
        #
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]

alist = [54,226,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)