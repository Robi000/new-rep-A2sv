from math import inf
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return nums1
        left = m-1
        right = n-1
        editAt = len(nums1) - 1
        while editAt != -1:
            # print(left , right , editAt)
            if (nums1[left] > nums2[right]):
                # print("if")
                # print ("==>" , nums1[left] , nums1[editAt] )
                nums1[editAt] = nums1[left]
                left -= 1
                if left == -1 or right == -1:
                    break
            elif (nums1[left] <= nums2[right]):
                # print("else")
                nums1[editAt] = nums2[right]
                right -=1

                if right == -1 or left == -1:
                    break
            editAt -= 1
        editAt -=1
        while  left != -1 or right != -1:
            # print("***", editAt , left , right)

            if right != -1:
                # print(nums2[right])
                nums1[editAt] = nums2[right]
                right -= 1
                if right == -1:
                    break
            elif left != -1:
                nums1[editAt] = nums1[left]
                left -= 1
                if left == -1:
                    break
            editAt -= 1
            if editAt < 0:
                break
        return (nums1)