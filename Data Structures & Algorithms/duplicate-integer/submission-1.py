class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(0, nums.__len__() - 1):
            if(nums[x]  == nums[x+1]):
                return True
        return False