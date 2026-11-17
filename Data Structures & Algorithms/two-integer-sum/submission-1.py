class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duplicateMap = {}

        for (i, j) in enumerate(nums):
            diff = target - j
            if diff in duplicateMap:
                return [duplicateMap[diff], i]
            duplicateMap[j] = i
        return List[duplicateMap]