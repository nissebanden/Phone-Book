class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    def remove(self, data):
        current_node = self.head
        if current_node is not None:
            if current_node.data == data:
                self.head = current_node.next
                current_node = None
                return
        while current_node is not None:
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node == None:
            return
        prev_node.next = current_node.next
        current_node = None

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next