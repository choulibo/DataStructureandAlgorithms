#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-9  @Author:libo  @FileName: 01_binary_search.py


def binary_search(alist,item):
    """
    二分查找 递归版本
    :param alist: 数组
    :param item: 查找元素
    :return: True False
    """
    # version 1
    # n = len(alist)
    # if n == 0:
    #     return False
    # mid = n // 2
    # if alist[mid] == item:
    #     return True
    # elif item < alist[mid]:
    #     return binary_search(alist[:mid],item)
    # else:
    #     return binary_search(alist[alist[mid+1]:],item)

    # version 2

    n = len(alist)
    if n == 0:
        return False

    mid = n // 2
    if alist[mid] == item:
        return True
    else:
        if item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)

if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binary_search(testlist, 17))
    print(binary_search(testlist, 13))