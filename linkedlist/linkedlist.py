class Node: 
  def __init__(self, num) -> None:
    self.data = num
    self.next = None

head = None
tail = None

head = Node(0)
tail = Node(0)
head.next = tail

while (1):
  num = int(input("자연수 입력:"))
  if num < 1: break

  next = Node(num)
  next.next = head.next
  head.next = next

curr = head.next

while curr is not tail:
  print(curr.data)
  curr = curr.next

