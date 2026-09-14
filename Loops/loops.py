# Python Loops

# 1. for loop
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# 2. for...in with string
for char in "Python":
    print(char)

# 3. range()
print(list(range(5)))          # 0 to 4
print(list(range(1, 6)))       # start, stop
print(list(range(1, 10, 2)))   # start, stop, step

# 4. for + range
for i in range(1, 6):
    print(i)

# 5. Start, Stop, Step
for i in range(10, 0, -1):
    print(i)

# 6. while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 7. break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 8. continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 9. Increment and decrement
x = 5
x += 1
print(x)

x -= 1
print(x)

# Python does NOT have x++ or x--
# Use x += 1 and x -= 1 instead.

# 10. Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# 11. pass
for i in range(3):
    pass