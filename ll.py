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
		self.previous = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	#returns number of nodes in LL
	def count(self):
		if self.head is None:
			return 0
		current_node = self.head
		count = 0
		while(current_node):
			count+=1
			current_node = current_node.next

		return count

	#adds node to head or tail of list depending on size.
	def add(self, node):
		print("Adding...", node.value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			node.previous = self.tail
			self.tail = node

	#adds node after specified data node. data: value to search for; node: item to insert
	def addAfter(self, data, node):
		print("Adding", node.value, "after", data, "...")
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
			current_node = self.head
			while(current_node):
				if current_node.next == self.tail:
					self.tail = current_node
					current_node.next = None
				current_node = current_node.next

	#deletes specified node
	def deleteNode(self, value):
		print("Deleting", value, "...")
		if self.count() == 0:
			print("Error! Empty LL!")
		elif self.count() > 0:
			current_node = self.head
			while (current_node):
				if current_node.next.value == value:
					current_node.next = current_node.next.next
					break
				current_node = current_node.next

	#toReplace: value to write over; replaceWith: value to insert
	def replaceNode(self, toReplace, replaceWith):
		print("Replacing", toReplace, "with", replaceWith)

		current_node = self.head
		while(current_node):
			if current_node.value == toReplace:
				current_node.value = replaceWith
				break
			current_node = current_node.next

	#prints node values to console
	def printList(self):
		temp = self.head
		ls = []
		while(temp):
			ls.append(temp.value)
			temp = temp.next

		print(ls)

	#reverse print doubly LL
	def printReverse(self):
		print("Printing doubly linked list in reverse order...")
		ls = []
		flag = False
		if self.count() > 0:
			current_node = self.tail
			while(not flag):
				ls.append(current_node.value)
				if (current_node.previous is None):
					flag = True
				current_node = current_node.previous

			print(ls)
			
	#reverses a LL given it's head
	def reverse(head):
		if head:
			currentNode = head
			prev = head
			old_head = None
			tmp = None
			while(currentNode):
				if not currentNode.next:
					currentNode.next = prev
					head = currentNode
					old_head.next = None
					return head
				else:
					if currentNode is not head:
						tmp = currentNode.next
						currentNode.next = prev
				else:
					old_head = currentNode
			prev = currentNode
			currentNode = tmp if tmp else currentNode.next

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

#replace specified node
	llist.replaceNode(1,"me")
	llist.printList()
	print("size...", llist.count())

#print LL in reverse order
	llist.printReverse()
