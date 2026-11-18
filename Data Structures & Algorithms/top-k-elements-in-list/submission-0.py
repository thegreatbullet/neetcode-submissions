class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}

        for i in range(len(nums)):
            new_dict[nums[i]] = new_dict.get(nums[i], 0) + 1

        newest_dict = sorted(new_dict, key=lambda num: new_dict[num], reverse = True)
        return newest_dict[:k]