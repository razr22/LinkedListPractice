'''
@Author: Zain Quraishi
@Date: 11/06/2019
@Description: Linked List manipulation practice
'''
import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	#prints node values to console
	def printList(self):
		temp = self.head
		ls = []
		while(temp):
			ls.append(temp.value)
			temp = temp.next

		print(ls)

	#returns number of nodes in LL
	def count(self):
		if self.head is None:
			return 0
		currentNode = self.head
		count = 0
		while(currentNode):
			count+=1
			currentNode = currentNode.next

		return count

	#adds node to head or tail of list depending on size.
	def add(self, node):
		print("adding...", node.value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	#adds node after specified data node
	def addAfter(self, data, node):
		print("adding", node.value, "after", data, "...")
		if self.head is not None:
			temp = self.head
			while(temp):
				if temp.value == data:
					tempTo = temp.next
					temp.next = node
					node.next = tempTo
					break
				temp = temp.next

	#deletes last node in LL
	def delete(self):
		print("Deleting tail node (", self.tail.value, ")...")
		if self.count() == 0:
			print("Error! Empty LL!")
		elif self.count() == 1:
			self.head = None
			self.tail = None
		elif self.count() > 0:
			currentNode = self.head
			while(currentNode):
				if currentNode.next == self.tail:
					self.tail = currentNode
					currentNode.next = None
				currentNode = currentNode.next

	#deletes specified node
	def deleteNode(self, value):
		print("Deleting", value, "...")
		if self.count() == 0:
			print("Error! Empty LL!")
		elif self.count() > 0:
			currentNode = self.head
			while (currentNode):
				if currentNode.next.value == value:
					currentNode.next = currentNode.next.next
					break
				currentNode = currentNode.next
				
if __name__=="__main__":
	llist = LinkedList()

	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node("OSR")

#add nodes to LL
	llist.add(node1)
	llist.add(node2)
	llist.add(node3)
	llist.add(node4)

	llist.printList()
	print("size...", llist.count())

#add node after specified node in LL
	node5 = Node(5)
	llist.addAfter(2, node5)
	llist.printList()
	print("size...", llist.count())

#delete last node in LL
	llist.delete()
	llist.printList()
	print("size...", llist.count())

#deletes specified node from LL
	llist.deleteNode(5)
	llist.printList()
	print("size...", llist.count())