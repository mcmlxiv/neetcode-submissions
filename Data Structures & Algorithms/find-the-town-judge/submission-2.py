class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing = defaultdict(int)
        incoming = defaultdict(int)

        for src, dist in trust:
            outgoing[src] += 1
            incoming[dist] +=1
        
        for i in range(n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        
        return -1