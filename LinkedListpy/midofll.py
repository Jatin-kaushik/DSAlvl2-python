class Node:
    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def addfirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    
    def addlast(self,data):
        node = Node()
        node.data = data
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            
    def display(self, node):
        while(node != None):
            print(str(node.data) + "->", end ="")
            node = node.next
        print("null")
    def midofll(self):
        stemp = self.head
        ftemp = stemp
        while ftemp.next != None and ftemp.next.next != None:
            # print(stemp.data)
            stemp = stemp.next
            ftemp = ftemp.next.next 
        self.display(stemp)

# def main():
inp = input()
# print(inp)
arr = inp.split("->")
# print(arr)
if "null" in arr:
    arr.remove("null")

arr = [int(i) for i in arr]
ll = LinkedList()
for i in arr:
    # print(i)
    ll.addlast(i)
ll.midofll()
    
        