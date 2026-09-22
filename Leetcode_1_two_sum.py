class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      #Brute force solution  
      '''
        
        for i in range (len(nums)) :
            for j in range  (i+1,len(nums)):
                if nums[i] + nums [j] == target :
                    return [i,j]
        '''
      #Hashmap solution
        tracking = {}
        for i,j in enumerate (nums):
            compliment = target - j
            if compliment in tracking :
                return [i,tracking[compliment]]  
            tracking [j] = i       
