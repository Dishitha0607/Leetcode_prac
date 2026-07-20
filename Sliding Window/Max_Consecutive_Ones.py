class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        current_count = 0
        max_count = 0
        n=len(nums)
        i=0

        while (i<n):
            if(nums[i]==1):
                current_count+=1
                i+=1
            
            else:
                max_count = max(max_count,current_count)
                current_count = 0
                i+=1
        return (max(max_count,current_count))
