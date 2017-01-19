#IMPORTANT: stack and class defs are NOT CORRECT!!
# class Stack:

# 	top = None 

# 	def __init__(self, data):
# 		self.next = None 
# 		self.data = data

# 	def pop(self):
# 		if Stack.top == None:
# 			print "Empty Stack Exception"
# 		else:
# 			item = Stack.top.data
# 			Stack.top = Stack.top.next
# 			return item

# 	def push(self, item):
# 		t = Stack(item)
# 		t.next = Stack.top
# 		Stack.top = t

# 	def peek(self):
# 		if Stack.top == None:
# 			print "Empty Stack Exception"
# 		else:
# 			return Stack.top.data 

# 	def isEmpty():
# 		return top == None 


# class Queue:

# 	first = None 
# 	last = None 

# 	def __init__(self, data):
# 		self.next = None 
# 		self.data = data 

# 	def add(item):
# 		t = Queue(item)
# 		if Queue.last != None:
# 			Queue.last.next = t
# 		Queue.last = t 
# 		if Queue.first == None:
# 			Queue.first = Queue.last 

# 	def remove():
# 		if Queue.first == None:
# 			print "No Such Element Exception"
# 		data = Queue.first.data 
# 		Queue.first = Queue.first.next 
# 		if Queue.first == None:
# 			Queue.last = None 
# 		return data 

# 	def peek():
# 		if Queue.first == None:
# 			print "Empty Stack Exception" 

# 		return Queue.first.data

# 	def isEmpty():
# 		return Queue.first == None

#3.1
#ThreeInOneStack:...IMPORTANT: just assume that the "clear" value is 0
class FixedMultiStack:
	
	numStacks = 3 
	
	def __init__(self, stackSize):
		self.stackCapacity = stackSize
		self.values = [0] * FixedMultiStack.numStacks * self.stackCapacity  
		self.sizes =  [0] * FixedMultiStack.numStacks 

	def indexOfTop(self, stacknum):
		offset = stacknum * self.stackCapacity 
		size = self.sizes[stacknum]
		topindex = offset + size - 1  
		return self.values[topindex]

	def isEmpty(self, stacknum):
		if self.sizes[stacknum] == 0:
			return True
		else:
			return False 

	def isFull(self, stacknum):
		if self.sizes[stacknum] == self.stackCapacity:
			return True
		else:
			return False

	def push(self, stacknum, value):

		if self.isFull(stacknum) == True:
			print "This stack is full, so you cannot push more onto the stack"
		else:
			offset = stacknum * self.stackCapacity
			size = self.sizes[stacknum]
			topindex = offset + size - 1 
			newindex = topindex + 1
			self.values[newindex] = value 
			self.sizes[stacknum] = self.sizes[stacknum] + 1

	def pop(self, stacknum):
		if self.isEmpty(stacknum) == True:
			print "The stack is empty, so you cannot pop anything off of the stack"
		else:
			offset = stacknum * self.stackCapacity
			size = self.sizes[stacknum]
			topindex = offset + size - 1 
			self.sizes[stacknum] = self.sizes[stacknum] - 1
			self.values[topindex] = 0
			return self.values[topindex]

	def peek(self, stacknum):
		if self.isEmpty(stacknum) == True:
			print "The stack is empty, so there's nothing to peek at"
		else:
			offset = stacknum * self.stackCapacity
			size = self.sizes[stacknum]
			topindex = offset + size - 1 
			return self.values[topindex]

#3.2: Stack Min
#if just ONE STACKMIN TOTAL, each initialization is a node but you can only have ONE MINSTACK total 
#MAIN IDEA: If we kept track of the minimum at each state, we would be able to easily know the minimum.
#We can do this by having each node record what the minimum beneath itself is. Then to find the min,
#you just look at what the top element thinks is the min. 
class StackMin:

	top = None 

	def __init__(self, data, prevsmall):
		self.next = None 
		self.data = data
		if prevsmall < data:
			self.smallest = prevsmall
		else: 
			self.smallest = data 

		self.min = data 

	@staticmethod
	def pop():
		if Stack.top == None:
			print "Empty Stack Exception"
		else:
			item = StackMin.top.data
			StackMin.top = StackMin.top.next
			return item

	@staticmethod
	def push(item):
		if StackMin.top == None:
			t = StackMin(item, item)
		else:
			t = StackMin(item, StackMin.top.smallest)
		t.next = StackMin.top
		StackMin.top = t

	@staticmethod
	def peek():
		if StackMin.top == None:
			print "Empty Stack Exception"
		else:
			return StackMin.top.data 

	@staticmethod
	def isEmpty():
		return StackMin.top == None 

	@staticmethod
	def minimum():
		return self.smallest 

#MULTIPLE STACKMINS, meaning the traditional Nodes filling up stacks implementations
class StackMin2Node:

	def __init__(self, data, prevsmall):
		self.data = data
		if prevsmall < data:
			self.smallest = prevsmall
		else:
			self.smallest = data

class StackMin2:

	def __init__(self):
		self.top = None
		self.smallest = None 

	def pop(self):
		if self.top == None:
			print "Empty Stack Exception"
		else:
			item = self.top.data
			self.top = self.top.next 
			return item 

	def push(self, item):
		if self.top == None:
			t = StackMin2Node(item, item)
			
		else:
			t = StackMin2Node(item, self.top.smallest)
			t.next = self.top
		self.top = t

	def peek(self):
		if self.top == None:
			print "Empty Stack Exception"
		else:
			return self.top.data

	def isEmpty(self):
		return self.top == None 

	def minimum(self):
		if self.top == None:
			print "Empty Stack Exception"
		else:
			return self.top.smallest

#3.3: Stack of Plates : We have to have 3 classes: Node at the bottom level, Stacks made up of nodes, and a SetOfStack composed of a set of stacks
#have a set of stacks, each of which remembers the previous stack using "oldStack"
#When a stack is full (each stack has a given capacity) we just create a new stack and set its previous stack to the current stack and replace
#the current stack with this new stack. We keep track of how many nodes there are on a stack by having an attribute called numnodes and incrementing
#it by 1 everytime we push and subract 1 everytime we pop   
class Node: 

	def __init__(self, data):
		self.data = data
		self.next = None 

class CapacityStack:

	def __init__(self, capacity):

		self.capcity = capacity 
		self.numnodes = 0 
		self.top = None 
		self.oldStack = None 

	def push(self, data):
		newnode = Node(data)
		newnode.next = self.top 
		self.top = newnode 
		self.numnodes = self.numnodes + 1

	def pop(self):
		if self.top == None: 
			print "There is nothing on this stack"
			return None
		else:
			temp = self.top.data
			self.top = self.top.next 
			self.numnodes = self.numnodes - 1
			return temp 

	def peek(self):
		if self.top == None: 
			print "There is nothing on this stack"
			return None
		else:
			return self.top.data

	def isEmpty(self):
		if self.top == None:
			return True 
		else:
			return False 

class SetOfStacks:

	def __init__(self, capacity):
		
		self.currentstack = CapacityStack(capacity)
		self.capacity = capacity 

	def push(self, data):
		if self.currentstack.numnodes == self.capacity:
			newstack = CapacityStack(self.capacity)
			newstack.push(data)
			newstack.oldStack = self.currentstack
			self.currentstack = newstack 

		else:
			self.currentstack.push(data)

	def pop(self):
		if self.currentstack == None:
			print "There is nothing on this stack"
			return None
		if self.currentstack.numnodes == 1:
			self.currentstack.pop()
			self.currentstack = self.currentstack.oldStack 
		else:
			self.currentstack.pop()

	def peek(self):
		if self.currentstack.top == None:
			print "Empty Stack Exception"
		else:
			return self.currentstack.top.data

	def isEmpty(self):
		return self.currentstack.top == None 

#3.4: Implement a Queue via 2 Stacks; Idea: We have 2 stacks: a "adding" stack and a "removal" stack.
#When we add an element we add it to the "adding" stack. When we want to get the next element of the queue we have to push everything 
#on the adding stack to the removal stack except for the last element which then becomes the element we want to pop. Then we add everything
#back to the adding stack 

#First of all, Node is already implemented by 3.3


class Stack:

	def __init__(self):
		self.top = None

	def pop(self):
		if self.top == None:
			print "Empty Stack Exception"
		else:
			item = self.top.data
			self.top = self.top.next 
			return item 

	def push(self, item):
		t = Node(item)
		t.next = self.top
		self.top = t

	def peek(self):
		if self.top == None:
			print "Empty Stack Exception"
		else:
			return self.top.data

	def isEmpty(self):
		return self.top == None 


class QueueTwoStacks:

	def __init__(self):
		self.addingstack = Stack()
		self.removalstack = Stack()

	def pop(self):
		if self.addingstack.top == None:
			print "There is nothing on the stack"
		else: 
			temp = 0
			while self.addingstack.top != None:
				temp = self.addingstack.pop()
				self.removalstack.push(temp)
			self.removalstack.pop()
			while self.removalstack.top != None:
				self.addingstack.push(self.removalstack.pop())
			return temp 
				
	def peek(self):
		if self.addingstack.top == None:
			print "There is nothing on the stack"
		else: 
			temp = 0
			while self.addingstack.top != None:
				temp = self.addingstack.pop()
				self.removalstack.push(temp)
			while self.removalstack.top != None:
				self.addingstack.push(self.removalstack.pop())
			return temp 

	def push(self, data):
		self.addingstack.push(data)

	def isEmpty(self):
		return self.addingstack.top == None