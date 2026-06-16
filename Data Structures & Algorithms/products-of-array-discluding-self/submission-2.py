import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i != j:
                    total *= nums[j]
                #print(total)
            new_arr.append((int)(total))
        
        return new_arr

        