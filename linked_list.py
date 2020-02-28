class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def print_node(self):
        temp = self.head
        while temp:
            print(temp.data, '-->', end='')
            temp = temp.next
        print()

    def first_insert_node(self, new_data):
        print("\n After inserting new data:")
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def end_insert_node(self, new_data):
        print("Insert the data at end")
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def middle_insert_node(self, middle, new_data):
        print("middle insert the data ")
        if middle is None:
            print("There is no node")
            return
        new_node = Node(new_data)
        new_node.next = middle.next
        middle.next = new_node

    def deleting_node(self, key):
        print("delete the first")
        # import pdb;pdb.set_trace()
        headval = self.head
        if headval.data == key:
            self.head = headval.next
            headval = None
            return
        while headval is not None:
            if headval.data == key:
                break
            prev = headval
            headval = headval.next

        if headval == None:
            return
        prev.next = headval.next
        HeadVal = None


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.print_node()

    llist.reverse_list()
    llist.print_node()

    # llist.first_insert_node(4)
    # llist.print_node()
    # llist.end_insert_node(5)
    # llist.print_node()
    # llist.middle_insert_node(second.next, 10)
    # llist.print_node()
    # llist.deleting_node(10)
    # llist.print_node()
    # llist.deleting_node(5)
    # llist.print_node()


