from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Calculate the length of the boxes string
        num_boxes = len(boxes)
        # Initialize an array to hold the answer (number of operations for each box)
        operations = [0] * num_boxes 
        # Initialize a counter for the number of operations moving from left to right
        left_to_right_count = 0

        # Traverse the boxes from left to right to calculate the number of operations needed
        for i in range(1, num_boxes):
            if boxes[i - 1] == '1':  # If the previous box contains a ball, increment the count
                left_to_right_count += 1
            operations[i] = operations[i - 1] + left_to_right_count  # Cumulative sum of operations

        # Reset the counter for the number of operations when moving from right to left
        right_to_left_count = 0
        sum_operations = 0

        # Traverse the boxes from right to left to add remaining operations
        for i in range(num_boxes - 2, -1, -1):  # Start from the second last box
            if boxes[i + 1] == '1':  # If the next box contains a ball, increment the count
                right_to_left_count += 1
            sum_operations += right_to_left_count  # Accumulate operations
            operations[i] += sum_operations  # Add the number of operations from right to the current answer

        return operations
