class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0 
        j = len(skill) -1
        sum = 0
        ans = 0
        while i < j:
            if i == 0:
                sum = skill[i] + skill[j]
                ans += skill[i] * skill[j]
            else:
                if sum != skill[i] + skill[j]:
                    return -1
                ans += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return ans


            
            
            
                
                
                
                    