#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-9  @Author:libo  @FileName: 14_Merge_sort.py

def merge_sort(alist):
    """归并排序"""
    if 1 == len(alist):
        return alist
    n = len(alist)
    mid = n // 2

    left_sorted_li = merge_sort(alist[:mid])
    right_sorted_li = merge_sort(alist[mid:])

    # 定义两个游标
    left,right = 0,0

    # 定义一个空列表用于存放新的数据
    merge_sorted_li = []

    left_n = len(left_sorted_li)
    right_n = len(right_sorted_li)
    # 合并的循环条件
    while left< left_n and right < right_n:
        # 在
        if left_sorted_li[left]<= right_sorted_li[right]:
            merge_sorted_li.append(left_sorted_li[left])
            left += 1
        else:
            merge_sorted_li.append(right_sorted_li[right])
            right += 1
    # 最后循环最大值及可能后续更大值，下面只有一个有值，另一个为空列表
    merge_sorted_li += left_sorted_li[left:]
    merge_sorted_li += right_sorted_li[right:]
    return merge_sorted_li


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before sort: %s" % alist)
    sorted_alist = merge_sort(alist)
    print("after sort: %s" % alist)
    print("sorted new list: %s" % sorted_alist)
