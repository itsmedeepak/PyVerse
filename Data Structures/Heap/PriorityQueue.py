class Node:

	def __init__(self, value=None, priority=0):
		self.value = value
		self.priority = priority
		self.next = None

class priorityQueue:

	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next
    
	def insertNode(self, value, priority=0):
		"""
		Insert a new node into the priority queue.
		Higher `priority` values are served before lower ones.
		If priorities are equal the new node is placed after existing nodes of same priority (FIFO for same priority).
		"""
		newNode = Node(value, priority)
		# empty queue
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			# insert at head if new node has higher priority than current head
			if newNode.priority > self.head.priority:
				newNode.next = self.head
				self.head = newNode
			else:
				tempNode = self.head
				# traverse until we find a node with lower priority than newNode or reach end
				while tempNode.next is not None and tempNode.next.priority >= newNode.priority:
					tempNode = tempNode.next
				# insert after tempNode
				nextNode = tempNode.next
				tempNode.next = newNode
				newNode.next = nextNode
				if tempNode == self.tail:
					self.tail = newNode

	def traversePQ(self):
			if self.head is None:
				print("Priority Queue Is Empty!!")
			else:
				node = self.head
				while node is not None:
					print(f"{node.value}({node.priority})", end=" ")
					node = node.next

	def searchElement(self, nodeValue):
		if self.head is None:
			print("Priority Queue Is Empty!!")
		else:
			node = self.head
			while node is not None:
				if node.value == nodeValue:
					return str(node.value) + ": Value Found!!"
				node = node.next
		return "The value does not exist in the queue!!"
    
	def deleteNode(self, location):
		"""
		Delete node at a given position (0-based).
		For a typical priority-queue dequeue, call deleteNode(0) to remove the highest-priority element.
		"""
		if self.head is None:
			print("Priority Queue Is Empty!!")
		elif self.head.next is None:
			self.head = None
			self.tail = None
		elif location == 0:
			self.head = self.head.next
		else:
			tempNode = self.head
			index = 0
			while index < location - 1 and tempNode.next is not None:
				tempNode = tempNode.next
				index += 1
			# if location is out of bounds, do nothing
			if tempNode.next is None:
				print("Location out of range!!")
				return
			nextNode = tempNode.next
			tempNode.next = nextNode.next
			if tempNode.next is None:
				# updated tail
				self.tail = tempNode

	def deleteEntirePQ(self):
		if self.head is None:
			print("Priority Queue Is Empty!!")
		else:
			tempNode = self.head
			while tempNode:
				store = tempNode.next
				del tempNode.value
				del tempNode.priority
				tempNode = store
			self.head = None
			self.tail = None

PQ = priorityQueue()
PQ.insertNode('task_low', 1)
PQ.insertNode('task_high', 5)
PQ.insertNode('task_medium', 3)
PQ.insertNode('task_high2', 5)
print("Queue After Inserts:", end=" ")
PQ.traversePQ()
print()

print(PQ.searchElement('task_medium'))

# Dequeue highest priority (location 0)
PQ.deleteNode(0)
print("Queue After Dequeue (removed head):", end=" ")
PQ.traversePQ()
print()

# Remove entire queue
PQ.deleteEntirePQ()
PQ.traversePQ()

