# coding=utf-8
# 写链表的技巧
# 先让cur游标沿着链表移动，写新节点node指向,再写其他节点，None不用指定



class Node(object):
    """节点类"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList(object):
    """
    双向链表
    """

    def __init__(self, node=None):
        self.__head = node  # 私有属性，头节点

    def is_empty(self):
        """
        单链表是否是空
        :return: 如果是空，返回为真
        """
        return self.__head is None

    def length(self):
        """
        链表长度
        :return:
        """
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历列表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def search(self, item):
        """查找节点是否存在,存在True,返回真,否则返回False"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def add(self, item):
        """头部添加元素"""

        # 先创建一个保存item值的节点
        node = Node(item)
        # 将该节点的下一节点指向为头节点
        node.next = self.__head
        # 将头节点指向node节点
        self.__head = node
        if node.next:
            node.next.pre = node


    def append(self, item):
        """向链表尾部添加元素"""
        node = Node(item)
        # 如果链表是空
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 退出循环,cur指向尾节点
            node.pre = cur
            cur.next = node

    def insert(self, pos, item):
        """指点位置添加元素"""
        node = Node(item)
        # 若指定位置为第一元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置为最后一个元素，在尾部插入
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            # 在pos位置添加元素
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            # 先操作新节点
            # 将新节点指向下一节点
            node.next = cur
            node.pre = cur.pre
            # 将前后节点指向node节点
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        while cur is not None:
            # 找到了节点
            if cur.item == item:
                # 如果头部节点就是要删除的节点
                if cur == self.__head:
                    self.__head = cur.next  # 第二个节点指定为头部节点
                    if cur.next:
                        self.__head.pre = None  # 新的头部节点的pre指定为空
                else:
                    # 继续按照列表移动,python有自动回收机制
                    cur.pre.next = cur.next
                    # 如果删除的不是最后一个节点
                    if cur.next:
                        cur.next.pre = cur.pre
                return
            # 不是要找的元素，移动游标
            cur = cur.next


if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.length())  # 0

    ll.append(1)  #
    print(ll.length())  # 1
    ll.travel()  # 1

    ll.append(2)
    ll.travel()  # 1 2

    ll.add(3)
    ll.travel()  # 3 1 2

    ll.insert(0, 4)
    ll.travel()  # 4 3 1 2

    ll.insert(10, 5)
    ll.travel()  # 4 3 1 2 5

    ll.insert(2, 6)
    ll.travel()  # 4 3 6 1 2 5

    ll.remove(4)
    ll.travel()  # 3 6 1 2 5

    ll.remove(5)
    ll.travel()  # 3 6 1 2

    ll.remove(6)
    ll.travel()  # 3 1 2

    ll.remove(3)
    ll.travel()  # 1 2

    ll.remove(2)
    ll.travel()  # 1

    ll.remove(1)
    ll.travel()  #

"""
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在

"""
