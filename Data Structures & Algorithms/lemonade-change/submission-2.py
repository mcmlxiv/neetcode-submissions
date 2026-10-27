class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}

        for b in bills:
            if b == 5:
                change[b] += 1
            
            if b == 10:
                change[10] += 1
                if change[5] > 0:
                    change[5] -= 1
                else:
                    return False
            if b == 20:
                change[20] += 1
                if change[5] > 0 and change[10] > 0:
                    change[5] -= 1
                    change[10] -=1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        
        return True 
            
        