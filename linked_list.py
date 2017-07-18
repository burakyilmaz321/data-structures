'''
Linked list class with core methods
Credits: https://www.youtube.com/watch?v=9YddVVsdG5A

Usage:
some_list = LinkedList()
some_list.add('first node')
some_list.add('second node')
some_list.getSize()
>> 2
'''

class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    class Node():
        def __init__(self, element):
            self.element = element
            self.next = None

        def getNext(self):
            return self.next

        def getElement(self):
            return self.element

        def setNext(self, nextnode):
            self.next = nextnode

        def setElement(self, element):
            self.element = element

    def getSize(self):
        return self.length

    def getHead(self):
        return self.head

    def add(self, element):
        node = self.Node(element)
        if self.getHead() == None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.getNext() != None:
                currentNode = currentNode.getNext()                
            currentNode.setNext(node)
        self.length += 1

    def remove(self, element):
        currentNode = self.head
        if currentNode.getElement() == element:
            self.head = currentNode.getNext
        else:
            while currentNode.getElement() != element:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(currentNode.getNext())
        self.length -= 1

    def is_empty(self):
        return self.length == 0

    def index_of(self, element):
        currentNode = self.head
        index = -1
        while currentNode != None:
            index += 1
            if currentNode.getElement() == element:
                return index
            currentNode = currentNode.getNext()
        return -1

    def element_at(self, index):
        currentNode = self.head
        count = 0
        while count < index:
            coutn += 1
            currentNode = currentNode.getNext()
        return currentNode.getElement()

    def add_at(self, index, element):
        node = Node(element)

        currentNode = self.head
        currentIndex = 0

        if index == 0:
            node.setNext(currentNode)
            self.head = node
        else:
            while currentIndex < index:
                currentIndex += 1
                previousNode = currentNode
                currentNode = currentNode.getNext()
            node.setNext(currentNode)
            previousNode.setNext(node)
        self.length += 1

    def remove_at(self, index, element):
        currentNode = head
        currentIndex = 0
        if index < 0 | index >= length:
            return None
        else:
            while currentIndex < index:
                currentIndex += 1
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(currentNode.getNext())
        length -= 1
        return currentNode.getElement()
