# define a Node class for linked list
# __name__ & __main__ 
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
# http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do

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

# define an unordered list
class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        print("The List is empty.")
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.addNext(self.head)
        self.head = temp
        print("successful add.")
        
mylist = UnorderedList()
mylist.isEmpty()
mylist.add(12)
mylist.add(13)
print(mylist)
