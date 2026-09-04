class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            print(stones)
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            print(x,y)

            if y > x:
                heapq.heappush_max(stones, y - x)
        
        return stones[0] if stones else 0