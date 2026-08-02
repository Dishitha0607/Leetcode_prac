class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        l=0
        count=0
        prod=1

        if (k<=1):
            return 0

        for r in range(n):
            prod *= nums[r]
            while(prod>=k):
                prod //= nums[l]
                l+=1
            count += r-l+1
        return count
