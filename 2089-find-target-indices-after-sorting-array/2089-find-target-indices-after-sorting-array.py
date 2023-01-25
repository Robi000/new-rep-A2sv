class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0
        ans = []
        while  i < len(nums):
            if nums[i] != target:
                i += 1
                continue
            else:
                ans.append(i)
            i += 1
            
        return ans
            