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
        node = LinkedList.Node(value,None,None)

    def get_node(self,index):
        if index < 0 or index > self.size:
            raise Exception('size error')
        if index < self.size/2:
            tmp = self.begin_marker
            for i in range(0,self.size):
                tmp = tmp.next
        else:
            tmp = self.end_maker
            for i in range(self.size,0,-1):
                tmp = tmp.next
        return tmp