class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # create new node instance and fill it with data
        new_node = Node(data)

        # if linked list doesnt have a head/any items
        if not self.head:
            # set head to new node
            self.head = new_node
            return
        
        # search for next empty spot in list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # set next node to new node
        last_node.next = new_node

    def prepend(self, data):
        # create new node instance and fill it with data
        new_node = Node(data)

        # set new node to set the next value to be the head of the lislt
        new_node.next = self.head

        # update the head of the list to the new node
        self.head = new_node

    def delete_node(self, key):
        # start at beginning of list
        current_node = self.head

        # check if first item is the node we are looking for
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        # search through list for desired key
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return
        
        # link last node to the next node after current node
        prev.next = current_node.next

        # remove desired node
        current_node = None

    
    def print_list(self):

        # print all items of the list, starting from list head
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.prepend(5)
llist.print_list()

print("\n")
llist.delete_node(3)
llist.print_list()