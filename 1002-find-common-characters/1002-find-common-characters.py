class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordset = set(words[0])
        ans = []
        for i in wordset:
            minn = words[0].count(i)
            for j in range(1, len(words)): 
                if words[j].count(i) == 0:
                    break
                minn = min(words[j].count(i) , minn)
            else:
                ans.extend([i]*minn)
        return (ans)

