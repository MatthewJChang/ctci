#Chapter 2
import math 

class Node:

	def __init__(self, data):
		self.next = None 
		self.data = data

	def append_to_tail(d):
		end = Node(d)
		n = self 
		while n.next != None:
			n = n.next

		n.next = end

def createLinkedList(values):
	n = Node(values[0])
	original = n 
	for i in values[1:]:
		n.next = Node(i)
		n = n.next 

	return original 
#2.3
#Slow way O(n)
def deleteMiddleNode(n):
	prev_node = None 
	while n.next != None:
		n.data = n.next.data
		prev_node = n 
		n = n.next 
	prev_node.next = None 
#alternate solution:
#Fast way O(1)
def deleteMiddleNode2(n):
	n.data = n.next.data
	n.next = n.next.next 

#2.4
def Partition(n, x):
	first_smaller = False  
	original_smaller = None
	before_smaller = None 
	smaller = None
	first_larger = False 
	original_larger = None 	
	larger = None 

	while n != None:
		if n.data < x:
			if first_smaller == False:
				original_smaller = Node(n.data)
				smaller = original_smaller
				first_smaller = True 
			else:
				smaller.next = Node(n.data)
				before_smaller = smaller 
				smaller = smaller.next 
		else:
			if first_larger == False:
				original_larger = Node(n.data)
				larger = original_larger 
				first_larger = True 
			else:
				larger.next = Node(n.data)
				larger = larger.next 
		n = n.next 

	if smaller != None:
		smaller.next = original_larger
	else:
		original_smaller = original_larger 
	return original_smaller 

def SumListsBackwardsOrder(node1, node2):
	number1 = 0
	place1 = 1
	number2 = 0
	place2 = 1
	while node1 != None:
		number1 = number1 + place1 * node1.data
		node1 = node1.next 
		place1 = place1 * 10

	while node2 != None:
		number2 = number2 + place2 * node2.data
		node2 = node2.next 
		place2 = place2 * 10

	sum_numbers = number1 + number2 

	start_node = Node(3)
	current_node = start_node
	
	places = 0
	value = sum_numbers 
	while value != 0:
		value = value / 10
		places = places + 1

	power_of_ten = 1
	#power_of_ten = math.pow(10, places - 1)

	while places != 0: 
		digit = (sum_numbers // power_of_ten) % 10
		current_node.next = Node(digit)
		current_node = current_node.next 
		power_of_ten = power_of_ten * 10
		#power_of_ten = power_of_ten / 10
		places = places - 1

	return start_node.next 

def SumListsForwardsOrder(node1, node2):
	number1 = 0
	place1 = 1
	number2 = 0
	place2 = 1
	while node1 != None:
		number1 = number1 + place1 * node1.data
		node1 = node1.next 
		place1 = place1 * 10

	while node2 != None:
		number2 = number2 + place2 * node2.data
		node2 = node2.next 
		place2 = place2 * 10

	sum_numbers = number1 + number2 

	start_node = Node(3)
	current_node = start_node
	
	places = 0
	value = sum_numbers 
	while value != 0:
		value = value / 10
		places = places + 1

	#power_of_ten = 1
	power_of_ten = math.pow(10, places - 1)

	while places != 0: 
		digit = (sum_numbers // power_of_ten) % 10
		current_node.next = Node(digit)
		current_node = current_node.next 
		#power_of_ten = power_of_ten * 10
		power_of_ten = power_of_ten / 10
		places = places - 1

	return start_node.next 

#This solution treats the problem as an addition problem in the most basic sence, adding digits and carrying
def sumListsCarry(l1, l2, carry):

	if l1 == None and l2 == None and carry == 0:
		return None 

	#create new Node, 3 is dummy value
	result = Node(3)

	value = carry 
	#IMPORTANT: the two numbers may not be perfectly aligned, so sometimes you may have either l1 or l2 be None
	#while there are still nodes for the other number...so you must do TWO if statements and check both cases
	if l1 != None:
		value = value + l1.data 

	if l2 != None:
		value = value + l2.data

	result.data = value % 10

	#Recurse
	if l1 != None or l2 != None:
		l1next = None 
		l2next = None 
		carrynext = 0
		if l1 != None:
			l1next = l1.next 
		if l2 != None:
			l2next = l2.next
		if value >= 10:
			carrynext = 1
		more = sumListsCarry(l1next, l2next, carrynext)
		result.next = more 

	return result  
	
	








