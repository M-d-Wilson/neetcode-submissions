import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        prefix = 1

        for i in nums:
            new_arr.append(prefix)
            prefix *= i

        postfix = 1

        for i in reversed(range(len(nums))):
            new_arr[i] = new_arr[i] * postfix
            postfix *= nums[i]

        return new_arr

        