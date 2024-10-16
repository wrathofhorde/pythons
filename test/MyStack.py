class MyStack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.stack = [-1 for _ in range(self.size)]

    def __str__(self):
        return f"top:{self.top}, size:{self.size}, stack:{self.stack}"

    def push(self, data):
        if self.top == self.size:
            print("stack full")
            return

        self.stack[self.top] = data
        self.top += 1

    def pop(self):
        if self.top == 0:
            print("stack empty")
            return

        self.top -= 1
        top = self.stack[self.top]
        return top


if __name__ == "__main__":
    s1 = MyStack(3)
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    print(s1)
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()
    print(s1)
