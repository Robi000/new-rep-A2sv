class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordSet = [set(sett) for sett in words]
        i = 0
        count = 0
        while i < len(wordSet):
            j = i +1
            while j < len(wordSet):
                if wordSet[i] == wordSet[j]:
                    count += 1
                    # wordSet.remove(wordSet[j])
                j += 1
            i+= 1
        return count
        
            
        
            
        