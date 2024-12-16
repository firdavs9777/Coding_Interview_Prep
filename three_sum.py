from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

         # Sorting helps to avoid duplicates in the triplet combinations 
        nums.sort()
        for i in range(len(nums) - 2):
            # To avoid duplicate triplets, skip the same element
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, len(nums) - 1):
                # To avoid duplicate elements, skip the same number at the second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = -nums[i] - nums[j]

                # Find the third number using a loop 
                for k in range(j + 1, len(nums)):
                    if nums[k] == target:
                        triplets.add((nums[i], nums[j], nums[k]))

        return [list(triplet) for triplet in triplets]   
# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
