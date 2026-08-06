class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for w in strs:
            count = [0] * 26

            for char in w:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(w)
        return res.values()
