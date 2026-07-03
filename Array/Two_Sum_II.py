class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        # The time complexity - O(N)

        while (left < right):
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left+1,right+1]

            elif sum>target:
                right -= 1
            
            else:
                left += 1
