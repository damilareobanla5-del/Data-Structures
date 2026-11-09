stack = []

# Adding items to the stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print("Stack:", stack)

# Removing the top item
stack.pop()
print("After Pop:", stack)

# Showing the top item
print("Top item:", stack[-1])

# Adding another item
stack.append(60)
print("After Push:", stack)

# Checking if stack is empty
print("Is stack empty?", len(stack) == 0)

# Displaying all items
print("Final Stack:", stack)

# Output:
Stack: [10, 20, 30, 40, 50]
After Pop: [10, 20, 30, 40]
Top item: 40
After Push: [10, 20, 30, 40, 60]
Is stack empty? False
Final Stack: [10, 20, 30, 40, 60]
