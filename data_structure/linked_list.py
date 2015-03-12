#coding:utf-8
__author__ = 'mason'




class LinkedList(object):

    class Node(object):
        def __init__(self,value,prev,next):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self):
        self.begin_marker = LinkedList.Node(None,None,None)
        self.end_maker = LinkedList.Node(None,self.begin_marker,None)
        self.size = 0

    def add(self,value):
        node = self.get_node(self.size)
        self.add_before(self.size,value)

    def add_before(self,position_node,value):
        node = LinkedList.Node(value,position_node.prev,position_node)
        position_node.prev.next = node
        position_node.next = node

    def get_node(self,index):
        if index < 0 or index > self.size:
            raise Exception('size error')
        if index < self.size/2:
            tmp = self.begin_marker
            for i in range(0,index):
                tmp = tmp.next
        else:
            tmp = self.end_maker
            for i in range(self.size,index,-1):
                tmp = tmp.prev
        return tmp

    def __iter__(self):
        return LinkedListIter(self.begin_marker,self.end_maker)


class LinkedListIter(object):

    def __init__(self,begin_marker,end_marker):
        self.begin_marker = begin_marker
        self.end_marker = end_marker
        self.current = begin_marker.next
        self.count = 0

    def next(self):
        pass
