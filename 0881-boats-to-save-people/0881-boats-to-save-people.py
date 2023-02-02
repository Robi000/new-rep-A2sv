class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) -1 
        ans = 0
        ith = True
        num = 0
        while num < len(people):
            if people[i] + people[j] <= limit:
                ith = False
                i += 1
                j -= 1
                ans += 1
                num += 2
            else:
                j -=1 
                ans += 1
                num += 1

        return ans 
        
        