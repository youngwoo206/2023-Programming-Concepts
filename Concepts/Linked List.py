# Linked List:

class node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class linkedList:
    def __init__(self) -> None:
        self.head = node()

    def append(self, data):
        newNode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: list index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: list index out of range")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1


myList = linkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.erase(2)
myList.display()
