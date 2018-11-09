#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 12_quick_sort.py

def Quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    mid = alist[start]
    left = start  # 左边游标
    right = end  # 右边游标
    # left和right未相遇，游标就向中间移动
    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]

    # 从循环退出后,left与right相遇,上述操作只是为了把mid放到正确的位置
    alist[left] = mid

    # 对左边执行递归排序
    Quick_sort(alist, start, left - 1)
    # 对右边执行递归排序
    Quick_sort(alist, right+1, end)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    Quick_sort(li, 0, len(li) - 1)
    print(li)
