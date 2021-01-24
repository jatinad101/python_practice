import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("Prev_node cannot be none")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node


    def addatlast(self, new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last
        return

    def deleteNode(self, key):

        if self.head is None or key is None:
            return

        # case 1
        if self.head == key:
            self.head = key.next

        # case 2
        if key.next is not None:
            key.next.prev = key.prev

        # case 3
        if key.prev is not None:
            key.prev.next = key.next

        # there can be other cases as well


        gc.collect()




    def printdlist(self, node):
        # TODO: a check can be done for node is head or not
        # this code expect that user will pass head
        while(node is not None):
            print(node.data, end=" ")
            node = node.next





