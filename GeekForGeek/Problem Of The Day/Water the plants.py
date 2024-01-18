#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # Create a list of tuples representing sprinkler ranges sorted by end position in descending order
        sprinkler_ranges = sorted([(i - g, i + g) for i, g in enumerate(gallery) if g != -1], reverse=True)

        # Initialize variables for current position, maximum reachable position, and sprinkler count
        current_position, max_reachable_position, sprinkler_count = 0, 0, 0

        # Iterate until the entire gallery is covered
        while current_position < n:
            # Check if there are sprinkler ranges and the last range can cover the current position
            if sprinkler_ranges and sprinkler_ranges[-1][0] <= current_position:
                start, end = sprinkler_ranges.pop()
                max_reachable_position = max(max_reachable_position, end + 1)
            elif max_reachable_position > current_position:
                # Move to the next uncovered position and increment the sprinkler count
                current_position = max_reachable_position
                sprinkler_count += 1
            else:
                # Unable to cover the current position, return -1
                return -1

        # Return the total sprinkler count required to cover the gallery
        return sprinkler_count
