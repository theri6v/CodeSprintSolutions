class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start_index, unique_count):
            # Base Case: If the starting index reaches or exceeds the length of the string
            if start_index >= len(s):
                # Update the maximum number of unique splits
                nonlocal max_unique_splits
                max_unique_splits = max(max_unique_splits, unique_count)
                return
            # Try to split the string from the current index to all possible subsequent indexes
            for end_index in range(start_index + 1, len(s) + 1):
                # If this substring has not been seen before
                if s[start_index:end_index] not in seen_substrings:
                    # Add the substring to the set of seen substrings
                    seen_substrings.add(s[start_index:end_index])
                    # Continue splitting the rest of the string with one additional unique substring found
                    backtrack(end_index, unique_count + 1)
                    # Backtrack: remove the substring from the set to try other possibilities
                    seen_substrings.remove(s[start_index:end_index])

        # Initialize a set to keep track of seen substrings
        seen_substrings = set()
        # Initialize the maximum number of unique splits variable
        max_unique_splits = 1
        # Start the recursive backtracking process from the beginning of the string
        backtrack(0, 0)
        # Return the maximum number of unique splits found
        return max_unique_splits
