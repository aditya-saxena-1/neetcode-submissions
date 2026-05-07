class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        for i in range(len(nums)):
            p = target-nums[i]
            if p in nums and nums.index(p) != i:
                L.append(i)
                L.append(nums.index(p))
                break
        L.sort()
        return L
