class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1 
        if n == 2:
            return 2
        
        way = [0,1,2] 
        for i in range(3, n+1):
            way.append(way[i-1] + way[i-2])
        return(way[-1])