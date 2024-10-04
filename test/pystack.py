stack_pointer = 0
stack = [0 for _ in range(0, 10)]


def stack_push(val):
    global stack_pointer

    if stack_pointer >= len(stack):
        print("Stack Overflow")
        return False

    stack[stack_pointer] = val
    stack_pointer += 1  # stack pointer를 다음으로 이동
    return True


def stack_pop():
    global stack_pointer

    if stack_pointer <= 0:
        print("Stack Underflow")
        return None

    stack_pointer -= 1
    return stack[stack_pointer]


def is_stack_empty():
    global stack_pointer

    return stack_pointer == 0


def stack_size():
    global stack_pointer

    return stack_pointer


def stack_peek():
    global stack_pointer

    if stack_pointer == 0:
        return None

    return stack[stack_pointer - 1]


def stack_print():
    print("*" * 40)
    print(stack)
    print("*" * 40)


if __name__ == "__main__":
    stack_push(-1)
    for i in range(0, 10):
        stack_push(i)

    stack_print()
    print(f"peek: {stack_peek()}")
    print(f"pop: {stack_pop()}")
    print(f"pop: {stack_pop()}")
    print(f"size: {stack_size()}")

    for _ in range(0, 10):
        stack_pop()
