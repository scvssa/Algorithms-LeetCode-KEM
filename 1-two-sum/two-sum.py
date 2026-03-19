class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range (len(nums)):
            d = target - nums[i]
            if d in hash_map:
                return [hash_map[d], i]
            hash_map [nums[i]] = i 
           

