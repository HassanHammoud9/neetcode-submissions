class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        for num in nums:
            while num != 0:
                if num == 1:
                    count+=1
        return count
