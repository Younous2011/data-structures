# https://www.hackerrank.com/challenges/30-linked-list/problem?h_r=internal-search

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data, end=' => ')
            current = current.next
        print(None)

    def insert(self,head,data): 
        node = Node(data)
        if head == None:
            head = node
        else:
            current_node = head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
        return head

mylist = Solution()
T = [7, 8, 9, 1]
head=None
for i in range(len(T)):
    data = T[i]
    head = mylist.insert(head, data)    
mylist.display(head); 	  