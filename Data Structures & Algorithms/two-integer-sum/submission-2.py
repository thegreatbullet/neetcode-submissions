class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        for i, n in enumerate(nums):
            new_dict[n] = i

        for i, n in enumerate(nums):
            difference = target - n
            if difference in new_dict and new_dict[difference] != i:
                return [i, new_dict[difference]]

        return []