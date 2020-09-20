#Linked List left to right

class node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.start = None

#inserting node sequentially left to right
    def insertNode(self,value):
        newNode = node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

#displaying node    
    def displayNode(self):
        if self.start == None:
            print ('List Empty')
        else:
            temp = self.start
            while temp.next != None:
                print (temp.value,end = ' ')
                temp = temp.next
            print (temp.value)
            print (' ')

#inserting node at the beginning    
    def insertFirst(self,value):
        newNode = node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            self.start = newNode
            self.start.next = temp

#inserting node at the end    
    def insertLast(self,value):
        newNode = node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

#inserting node at particular index
    def indexInsert(self,value,index):
        newNode = node(value)
        if self.start == None and index == 0:
            self.start = newNode
        elif self.start != None and index == 0:
            temp = self.start
            self.start = newNode
            self.start.next = temp
        elif self.start == None and index != 0:
            print ('Invalid index')
        else:
            counter = 0
            temp = self.start
            while counter<index:
                temp1 = temp
                temp = temp.next
                counter = counter + 1
            if counter == index:
                temp3 = temp
                temp = newNode
                temp1.next = temp
                temp.next = temp3
            elif index == counter+1:
                temp.next = newNode
            else:
                print ('Invalid index')

#deleting node at paricular index
    def indexDelete(self,index):
        if self.start == None:
            print ('Linked List Empty')
        elif self.start.next == None:
            self.start = None
        else:
            counter = 0
            temp = self.start
            while counter<index:
                temp1 = temp
                temp = temp.next
                counter = counter + 1
            if counter == index:
                temp1.next = temp.next
            else:
                print ('Invalid index')

#length of linked list
    def listLength(self):
        if self.start == None:
            print (0)
        else:
            counter = 1
            temp = self.start
            while temp.next != None:
                temp = temp.next
                counter = counter + 1
            print (counter)



