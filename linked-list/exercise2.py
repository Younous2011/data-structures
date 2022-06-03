#!/bin/python3

import math
import os
from pickle import NONE
import random
import re
import sys
from tkinter.messagebox import NO

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def printL(node):
    print("_____")
    while node != None:
        print(node.data, sep=" => ")
        node = node.next
    print(None)

def reverse(llist):
    precedent = None
    current = llist
    while current != None:
        suivant = current.next
        current.next = precedent
        precedent = current
        print("c:", current.data)
        current = suivant
        printL(precedent)
    return precedent

if __name__ == '__main__':
    fptr = open("output.txt", "w")

    tests = 1

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
