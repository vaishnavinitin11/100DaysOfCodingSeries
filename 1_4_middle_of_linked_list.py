class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
        self.last=None

    #Adding a new node at the end of the linked list
    def add_node(self,node):
        if(self.last==None):
            self.head=Node(node)
            self.last=self.head
        else:
            self.last.next=Node(node)
            self.last=self.last.next

    def display(self):
        current=self.head
        while current is not None:
            print(current.key,end=" ")
            current=current.next

    def display_neighbour(self):
        current=self.head
        while current is not None:
            if(current.next!=None):
                print(current.next.key,end=" ")
            else:
                print("None", end=" ")
            current=current.next


ll=Linked_List()

ll.add_node(40)
ll.add_node(88)
ll.add_node(45)
ll.add_node(90)

ll.display()
ll.display_neighbour()