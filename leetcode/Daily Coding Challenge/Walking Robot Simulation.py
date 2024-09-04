class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direction vectors
        ans = 0
        d = 0  # 0 := north, 1 := east, 2 := south, 3 := west
        x = 0  # Initial x position
        y = 0  # Initial y position
        obstaclesSet = {(obs_x, obs_y) for obs_x, obs_y in obstacles}  # Convert obstacles to a set for faster lookup

        for c in commands:
            if c == -1:
                d = (d + 1) % 4  # Turn right
            elif c == -2:
                d = (d + 3) % 4  # Turn left
            else:
                for _ in range(c):
                    new_x = x + dirs[d][0]
                    new_y = y + dirs[d][1]
                    if (new_x, new_y) in obstaclesSet:
                        break
                    x = new_x
                    y = new_y

            ans = max(ans, x * x + y * y)  # Update the maximum distance squared

        return ans
