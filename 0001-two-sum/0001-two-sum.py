class Solution(object):
    def twoSum(self, nums, target):
        # Creating the empty dictionary.
        dic = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            # Finding the position and value in the dictionary

            if complement in dic:
                return [dic[complement], i]

            # Storing the values in dictionary
            dic[nums[i]] = i

        return []
            
