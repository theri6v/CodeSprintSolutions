class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize the deque with a fixed size of 'k'.
        """
        self.queue = [0] * k
        self.head = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Add an item at the front of the deque.
        Returns True if the operation is successful, otherwise False.
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            self.head = (self.head - 1 + self.capacity) % self.capacity
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Add an item at the rear of the deque.
        Returns True if the operation is successful, otherwise False.
        """
        if self.isFull():
            return False
        tail_index = (self.head + self.size) % self.capacity
        self.queue[tail_index] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Delete an item from the front of the deque.
        Returns True if the operation is successful, otherwise False.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Delete an item from the rear of the deque.
        Returns True if the operation is successful, otherwise False.
        """
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        Returns the front item, or -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        Returns the last item, or -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        tail_index = (self.head + self.size - 1) % self.capacity
        return self.queue[tail_index]

    def isEmpty(self) -> bool:
        """
        Check whether the deque is empty.
        Returns True if the deque is empty, otherwise False.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Check whether the deque is full.
        Returns True if the deque is at full capacity, otherwise False.
        """
        return self.size == self.capacity

# Example of how to use the MyCircularDeque class
# circular_deque = MyCircularDeque(3)
# print(circular_deque.insertLast(1))  # returns True
# print(circular_deque.insertLast(2))  # returns True
# print(circular_deque.insertFront(3)) # returns True
# print(circular_deque.insertFront(4)) # returns False, the queue is full
# print(circular_deque.getRear())      # returns 2
# print(circular_deque.isFull())       # returns True
# print(circular_deque.deleteLast())   # returns True
# print(circular_deque.insertFront(4)) # returns True
# print(circular_deque.getFront())     # returns 4
        
