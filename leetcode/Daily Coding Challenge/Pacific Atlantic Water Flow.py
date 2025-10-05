class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(cell, visited):
            if cell in visited:
                return
            visited.add(cell)
            r, c = cell
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs((nr, nc), visited)

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        for r in range(rows):
            dfs((r, 0), pacific)
            dfs((r, cols - 1), atlantic)
        for c in range(cols):
            dfs((0, c), pacific)
            dfs((rows - 1, c), atlantic)

        return list(pacific & atlantic)
