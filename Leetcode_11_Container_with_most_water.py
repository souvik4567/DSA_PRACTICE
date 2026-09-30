class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len (height) - 1
        max_height = 0
        while right > left:
            if height[left] < height[right] :
                max_height = max(height[left]*(right-left),max_height) 
                left +=1
            else :
                max_height = max(height[right]*(right-left),max_height)
                right -=1
        return max_height
