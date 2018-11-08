#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 11_insert_sort.py

def Insert_sort(alist):
    """插入排序"""

    for i in range(1,len(alist)):
        # 从第一个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
Insert_sort(alist)
print(alist)