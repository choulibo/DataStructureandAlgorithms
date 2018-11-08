#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-8  @Author:libo  @FileName: 06_stack.py


class Stack(object):
    """栈"""
    """
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
    """
    def __init__(self):
        """用于保存数据的真实容器"""
        self.__items = []

    def push(self,item):
        """添加元素到栈顶"""
        self.__items.append(item)  # 时间复杂度O(1)

    def pop(self):
        """弹出元素"""
        return self.__items.pop()  # 时间复杂度O(1)

    def peek(self):
        """返回到栈顶元素"""
        # return self.__items[-1]
        return self.__items[len(self.__items)-1]

    def is_empty(self):
        """判空"""
        return self.__items == []

    def size(self):
        """返回栈大小"""
        return len(self.__items)


if __name__ == '__main__':
     stack = Stack()
     stack.push("hello")
     stack.push("world")
     stack.push("libo")
     print(stack.size())
     print(stack.peek())
     print(stack.pop())
     print(stack.pop())
     print(stack.pop())