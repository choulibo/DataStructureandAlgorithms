#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-9  @Author:libo  @FileName: 02_binary_search_no_recursive.py

def binary_search(alist,item):
    """
    二分查找 非递归版本
    :param alist: 数组
    :param item: 待查找元素
    :return: True False
    """

    start = 0
    end = len(alist) -1

    while start <= end:
        mid = (start + end) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            end = mid - 1
        else :
            start  = mid + 1
    # 退出循环，表示没有找到
    return  False


if __name__ == '__main__':

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(testlist, 19))
    print(binary_search(testlist, 42))