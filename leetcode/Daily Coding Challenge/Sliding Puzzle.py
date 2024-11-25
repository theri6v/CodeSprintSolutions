from heapq import heappop, heappush
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        rows, cols = 2, 3
        start_state = ''.join(str(num) for row in board for num in row)
        target_state = '123450'

        def is_solvable(sequence: List[int]) -> bool:
            inv_count = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
            return inv_count % 2 == 0

        def heuristic(state: str) -> int:
            total_distance = 0
            for i, char in enumerate(state):
                if char != '0':
                    num = int(char) - 1
                    total_distance += abs(i // cols - num // cols) + abs(i % cols - num % cols)
            return total_distance

        sequence = [num for num in map(int, start_state) if num != 0]
        if not is_solvable(sequence):
            return -1

        queue = [(heuristic(start_state), start_state)]
        distances = {start_state: 0}

        while queue:
            _, state = heappop(queue)
            if state == target_state:
                return distances[state]

            zero_position = state.index('0')
            i, j = divmod(zero_position, cols)
            state_list = list(state)

            for delta_row, delta_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                x, y = i + delta_row, j + delta_col
                if 0 <= x < rows and 0 <= y < cols:
                    new_zero_pos = x * cols + y
                    state_list[zero_position], state_list[new_zero_pos] = state_list[new_zero_pos], state_list[zero_position]
                    next_state = ''.join(state_list)
                    state_list[zero_position], state_list[new_zero_pos] = state_list[new_zero_pos], state_list[zero_position]

                    if next_state not in distances or distances[next_state] > distances[state] + 1:
                        distances[next_state] = distances[state] + 1
                        heappush(queue, (distances[next_state] + heuristic(next_state), next_state))

        return -1
