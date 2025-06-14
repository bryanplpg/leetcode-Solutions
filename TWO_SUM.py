class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            i+=1
            y=target-nums[i]
            if y in nums:
                return[i,nums.index(y)]
        return[]
                   

            
           
    

            
        

        