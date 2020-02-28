class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(data= new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def print_list(self, node):
        while node is not None:
            print(node.data, '--> <--',end='')
            last = node
            node = node.next


dllist = DoublyLinkedList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.print_list(dllist.head)




