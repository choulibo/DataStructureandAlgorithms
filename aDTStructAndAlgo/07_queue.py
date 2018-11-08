#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 07_queue.py


class Queue(object):
    """队列"""
    """
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
    """


    def __init__(self):
        # 创建空间，存储数据
        self.items = []

    def is_empty(self):
        """判空"""
        return self.items == []

    def enqueue(self,item):
        """添加队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue("hello")
    queue.enqueue("world")
    queue.enqueue("libo")
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())