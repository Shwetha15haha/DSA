import typing
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # length of array
        n = len(nums)
        # how do you calculate indices? index starts from 0
        # so length = n then index is 0 to (n-1)
        # so for given nums , you have to get sum of each two elements and check against target     
        for i in range(n):
          for j in range(n):
            if i!=j and nums[i]<=nums[j]:
              sum = nums[i]+nums[j]
              if sum == target:
                  return [i, j]
                        
    
input1 = Solution()
result = input1.twoSum([2,7,11,15], target = 9)