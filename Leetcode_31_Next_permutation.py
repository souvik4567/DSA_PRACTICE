class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)-1,0,-1):
            if nums[i-1]< nums[i]:
                for j in range (len(nums)-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        self.swap(nums,i-1,j)
                        self.list_rev(nums,i)
                        break
                break        
        else :
            self.list_rev(nums,0)

        return nums

    def swap (self,arr,i,j): 
        arr[i],arr[j] = arr[j] ,arr[i]

    def list_rev (self,arr,start):
        l =start
        r = len(arr) - 1
        while  l < r :
            self.swap(arr,l,r)
            l+=1
            r-=1


        
