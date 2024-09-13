from icecream import ic

# ic.disable()

class Node:
  def __init__(self, data = 0) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = Node()
    self.curr = None
    self.prev = None
    self.numOfData = 0
    self.comp = None

  def finsert(self, data) -> None:
    node = Node(data=data)
    node.next = self.head.next
    self.head.next = node
    self.numOfData += 1
    ic(f"{node.data} is inserted at 1st pos, size:{self.numOfData}")

  def sinsert(self, data) -> None:
    pass

  def insert(self, data) -> None:
    if self.comp is None:
      self.finsert(data=data)
    else:
      self.sinsert(data=data)

  def first(self, node) -> bool:
    self.prev = self.head
    self.curr = self.prev.next
    
    if self.curr is None:
      return False

    node.data = self.curr.data

    return True

  def next(self, node) -> bool:
    if self.curr.next is None:
      return False
    
    self.prev = self.curr
    self.curr = self.curr.next
    node.data = self.curr.data

    return True

  def remove(self) -> any:
    if self.curr is None:
      print("list empty, remove nothing")

    data = self.curr.data
    self.prev.next = self.curr.next
    self.curr = self.prev
    self.numOfData -= 1

    ic(f"remove {data}")

    return data

  def count(self) -> int:
    return self.numOfData
  
  def sortrule(self, comp) -> Node:
    self.comp = comp

  def remove_all(self) -> None:
    node = Node()

    if self.first(node) is True:
      self.remove()
      while self.next(node) is True:
        self.remove()

  def print(self) -> None:
    list = []
    node = Node()

    if self.first(node) is True:
      list.append(node.data)
      while self.next(node) is True:
        list.append(node.data)

    print(list)

if __name__ == "__main__":
  node = Node()
  list = LinkedList()
  list.print()
  list.insert(3)
  list.insert(2)
  list.insert(1)
  list.insert(8)
  list.print()
  list.remove_all()
  list.print()
