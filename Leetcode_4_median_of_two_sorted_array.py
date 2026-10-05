class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) < len(nums1) :
            nums1,nums2 = nums2,nums1

        m = len(nums1)
        n = len(nums2)

        left , right = 0 , m
        left_part = ( m + n  + 1) // 2 #This is left part of the final array

        while left <= right :
            m_part  = (left + right) // 2 # how much number should be coming from nums1 array 
            n_part = left_part -  m_part # how much number should be coming from nums2 array

            last_m  = nums1 [m_part-1] if m_part >0 else float ('-inf')
            remain_first_m = nums1[m_part] if m_part < m  else float ('inf')
            last_n = nums2[n_part-1] if n_part >0 else float ('-inf')
            reamain_first_j = nums2[n_part] if n_part < n  else float ('inf')


            if last_m <= reamain_first_j and last_n <= remain_first_m :
                if (m+n)%2 == 0:
                    return ((max(last_m,last_n)+min(remain_first_m,reamain_first_j))/2.0)
                else :
                    return (max(last_m,last_n))

            elif last_m > reamain_first_j:
                right = m_part - 1
            else :
                left  = m_part + 1     



