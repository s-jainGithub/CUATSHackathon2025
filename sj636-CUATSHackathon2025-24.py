class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Using dictionaries to access the power set
        power_set = {():1}
        lower_set = {():1}
        nums = sorted(nums)
        for n in nums:
            for p in lower_set:
                new = list(p)+[n]
                t = tuple(new)
                if t not in power_set:
                    power_set[t] = 1
            lower_set = power_set.copy()
        return [list(p) for p in power_set.keys()]
