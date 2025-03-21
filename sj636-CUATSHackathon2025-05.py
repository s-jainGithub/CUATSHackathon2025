class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        C = [[]]
        for n in nums:
            for o in C:
                output.append(o+[n])
            C = output.copy()
        return output
