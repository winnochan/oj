#!/usr/bin/env python

from typing import List


class Solution:
    def o_n_squared(self, nums: List[int]) -> int:
        """
        O(n^2) solution

        define dp[i] as length of longest increasing subsequence which ends with nums[i-1]
        """

        nlen = len(nums)
        maxl = 1 if nlen > 0 else 0
        dp = [1] * (nlen)

        for i in range(nlen):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    if dp[i] > maxl:
                        maxl = dp[i]

        return maxl

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.o_n_squared(nums)


def test():
    s = Solution()
    print(s.lengthOfLIS([]))
    print(s.lengthOfLIS([0]))
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))


test()
