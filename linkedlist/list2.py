from icecream import ic

# ic.disable()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.len = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail

    def is_empty(self):
        return self.head.next is self.tail

    def insert(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.len += 1

        ic(f"{data} inserted, size:{self.len}")

        return node

    def print(self):
        curr = self.head.next
        while curr is not self.tail:
            print(curr.data)
            curr = curr.next

    def find(self, data):
        curr = self.head.next
        while curr is not self.tail:
            if curr.data is data:
                return curr
            curr = curr.next

        return None
    
    def delete(self, data):
        prev = self.head
        curr = self.head.next

        while curr is not self.tail:
            if curr.data is data:
                self.len -= 1
                prev.next = curr.next

                ic(f"{data} deleted, size:{self.len}")
                return True
            else:
                prev = curr
                curr = curr.next

        ic(f"{data} is not found")
        return False

    def add(self, data):
        prev = self.head
        curr = self.head.next

        while curr is not self.tail:
            prev = curr
            curr = curr.next

        node = Node(data)
        prev.next = node
        node.next = curr
        self.len += 1
        ic(f"{data} added, size:{self.len}")

    def size(self):
        ic(f"length of list:{self.len}")
        return self.len

if __name__ == "__main__":
    list = List()
    list.add(1)
    list.insert(2)
    list.insert(3)
    list.add(4)
    list.print()
    print(list.delete(5))
    list.add(6)
    print(list.delete(3))
    print(list.delete(1))
    list.print()
    list.size()
