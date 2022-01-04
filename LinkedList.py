class Node:

	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None


#insertion and examples

linkL = LinkedList()

linkL.head = Node(1)
second = Node(2)
third = Node(3)

linkL.head.next = second   #connect head to node 2
second.next = third		   #connects node 2 to 3