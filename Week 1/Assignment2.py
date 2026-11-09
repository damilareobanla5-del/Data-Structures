queue = []

# Adding items to the queue
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print("Queue:", queue)

# Removing the first item
queue.pop(0)
print("After Dequeue:", queue)

# Showing the first item
print("Front item:", queue[0])

# Checking if queue is empty
print("Is queue empty?", len(queue) == 0)

# Displaying the queue
print("Final Queue:", queue)

# Expected Output:
# Queue: [10, 20, 30, 40, 50]
# After Dequeue: [20, 30, 40, 50]
# Front item: 20
# Is queue empty? False
# Final Queue: [20, 30, 40, 50]


# Applications of Queue:
# Printer machines.
# Customer service.
# Computer task scheduling.
# Ticket booking.
# Network communication.
# Call centres.
