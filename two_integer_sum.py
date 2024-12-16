class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)): 
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
# Input: numbers = [1,2,3,4], target = 3
#Output: [1,2]

