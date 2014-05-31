# define a Node class for linked list
class Node:
	def __init__ (self,initdata):
		self.data = initdata
		self.next = None
	def getData (self):
		return self.data
	def getNext (self):
		return self.next
	def addData(self, addedData):
		self.data = addedData
	def addNext(self, nextNode):
		self.next = nextNode
		

temp = Node("hello")
print(temp.getData())
temp.addData(98)
print(temp.getData())