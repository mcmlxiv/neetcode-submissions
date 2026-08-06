class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26

            for char  in word:
                alphabet[ord(char) - ord('a')]  += 1
            
            output[tuple(alphabet)].append(word)
        return output.values()
 