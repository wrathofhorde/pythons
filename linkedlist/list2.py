class Node:
    def __init__(self, num):
        self.data = num
        self.next = None


class List:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail

    def insert(self, num):
        node = Node(num)
        node.next = self.head.next
        self.head.next = node
        return node

    def print(self):
        curr = self.head.next
        while curr is not self.tail:
            print(curr.data)
            curr = curr.next

    def find(self, num):
        curr = self.head.next
        while curr is not self.tail:
            if curr.data == num:
                return curr
            curr = curr.next

        return None


list = List()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.print()

ret = list.find(3)

if ret is not None:
    print(ret.data)
else:
    print("not found")
