class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right  = len(height) - 1 
        l_max = height[left]
        r_max = height[right]
        total = 0
        while left < right:
            if height[left] < height[right] :
                l_max = max(l_max,height[left])
                total = (l_max - height[left]) + total
                left +=1
            else :
                r_max = max(r_max,height[right])
                total = (r_max - height[right]) + total
                right -=1
        return total
