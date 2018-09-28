class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        maximum = 2147483647
        start = 1
        end = maximum
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid > x:
                end = mid - 1
            elif (mid + 1) * (mid + 1) > x:
                return mid
            else:
                start = mid + 1