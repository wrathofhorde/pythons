file = open("write.txt", "w", encoding="utf-8")
print("Hello, World!", file=file)
print("파이썬이 쉽다는 것은 다른 프로그래밍 언어에 비해 쉽다는 것.", file=file)
print("프로그래밍 자체가 쉽다는 것을 의미하는 것이 아님.", file=file)
print("유튜버들에게 속지 말 것.", file=file)
file.close()