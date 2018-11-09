#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 13_shell_sort.py

def Shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    # 现分成两列
    gap = n // 2
    # 循环插入排序，直到成一排插入排序后循环结束
    while gap >= 1:
        for i in range(gap,n):
            # 游标指向第二个元素
            j = i
            # 从第二个元素开始，所以是j-gap>= 0时，一直
            while (j-gap) >= 0:
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]
                    j -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    Shell_sort(li)
    print(li)
