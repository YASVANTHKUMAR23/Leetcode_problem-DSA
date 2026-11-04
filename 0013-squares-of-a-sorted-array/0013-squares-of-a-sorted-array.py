class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        
        while right >= left:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            nums[left] = left_square
            nums[right] = right_square

            left += 1
            right -= 1

        nums.sort()
        return nums

        
        