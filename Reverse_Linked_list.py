class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverseList(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


llist = LinkedList()

llist.push(20)
llist.push(4)
llist.push(59)
llist.push(21)

print("Givan linked list is :")
llist.print_list()

print('Reverse the list')
llist.reverseList()
llist.print_list()



