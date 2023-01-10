class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        ans = []
        for num in nums:
            if num%2 == 0:
                even += num
                
        for i , j in queries:
            num = nums[j] + i
            if num % 2 == 0 and nums[j] % 2 == 0:
                even = even - nums[j] + num
                ans.append(even)
            elif num % 2 == 1 and nums[j] % 2 == 0:
                even = even - nums[j]
                ans.append(even)
            elif num %2 == 0 and nums[j] % 2 == 1 :
                even = even + num
                ans.append(even)
            else:
                ans.append(even)
            nums[j] = num
        return ans
            