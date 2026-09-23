class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [[0,0,0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if (r,c) == (ROWS- 1, COLS - 1):
                return diff
            
            for dr, dc in directions:
                newR, newC = dr+r, dc+c

                if(newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS or (newR, newC) in visited):continue

                newDiff = max(diff, 
                abs(heights[r][c] - heights[newR][newC]))

                heapq.heappush(minHeap,[newDiff, newR, newC])
        
        return 0

