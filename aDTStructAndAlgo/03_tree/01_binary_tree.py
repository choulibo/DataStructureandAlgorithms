#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-11-9  @Author:libo  @FileName: 01_binary_tree.py


class Node(object):
    """节点类"""

    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class BinaryTree(object):
    """二叉树"""

    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """
        广度优先遍历方式添加节点
        :param item:
        :return:
        """
        if self.root is None:
            self.root = Node(item)
        else:
            # 新建一个队列，用于保存数据
            queue = []
            queue.append(self.root)
            while len(queue) > 0:
                node = queue.pop(0)
                # 左子树为空,添加元素
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                # 右子树为空，添加元素
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)

    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item, end=' ')
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def preorder_travel(self, root):
        """先序"""
        if root:
            print(root.item, end=' ')
            # root.lchild 作为下一递归的root节点
            self.preorder_travel(root.lchild)
            # root.rchild 作为下一递归的root节点
            self.preorder_travel(root.rchild)

    def inorder_travel(self, root):
        """中序"""
        if root:
            self.inorder_travel(root.lchild)
            print(root.item, end=' ')
            self.inorder_travel(root.rchild)

    def postorder_travel(self, root):
        """先序"""
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end=' ')


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadh_travel()
    print("")
    tree.preorder_travel(tree.root)
    print("")
    tree.inorder_travel(tree.root)
    print("")
    tree.postorder_travel(tree.root)
    print("")