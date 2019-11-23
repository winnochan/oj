from typing import List


class Solution:
    '''
    define f(i, j, k) = nums[i] + nums[j] + nums[k], where i < j < k.
    find all possible solutions for f(i, j, k) = 0.
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        threeSumMap = {}
        for i in range(1, n - 1):
            j, k = i - 1, i + 1

            while j >= 0 and k < n:
                three = nums[i] + nums[j] + nums[k]
                if three > 0:
                    j -= 1
                elif three < 0:
                    k += 1
                else:
                    threeSumMap[(nums[j], nums[i],
                                 nums[k])] = [nums[j], nums[i], nums[k]]

                    j -= 1
                    while j >= 0:
                        if nums[j] != nums[j + 1]:
                            break
                        j -= 1
                    k += 1
                    while k < n:
                        if nums[k] != nums[k - 1]:
                            break
                        k += 1

        return list(threeSumMap.values())


s = Solution()
t = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(t))
