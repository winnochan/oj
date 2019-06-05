#!/usr/bin/env python

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, a: List[int], l: int, m: int) -> int:
        """
        O(n ^ 2)
        """
        n = len(a)
        max_sum = 0

        # case 1: L on the left side and M on the right side.
        ls = 0
        le = n - l - m
        ms = l
        me = n - m
        lsum = []
        msum = []
        # O(n)
        for i in range(n):
            if ls <= i <= le:
                if not lsum:
                    lsum.append(sum(a[i:i + l]))
                else:
                    lsum.append(lsum[-1] - a[i - 1] + a[i + l - 1])
            if ms <= i <= me:
                if not msum:
                    msum.append(sum(a[i:i + m]))
                else:
                    msum.append(msum[-1] - a[i - 1] + a[i + m - 1])

        # O(n * n)
        for i in range(len(lsum)):
            for j in range(i, len(msum)):
                tmp_sum = lsum[i] + msum[j]
                if tmp_sum > max_sum:
                    max_sum = tmp_sum

        if l == m:
            return max_sum

        # case 2: L on the right side and M on the left side.
        ls = m
        le = n - l
        ms = 0
        me = n - l - m
        lsum = []
        msum = []
        # O(n)
        for i in range(n):
            if ls <= i <= le:
                if not lsum:
                    lsum.append(sum(a[i:i + l]))
                else:
                    lsum.append(lsum[-1] - a[i - 1] + a[i + l - 1])
            if ms <= i <= me:
                if not msum:
                    msum.append(sum(a[i:i + m]))
                else:
                    msum.append(msum[-1] - a[i - 1] + a[i + m - 1])

        # O(n * n)
        for i in range(len(lsum)):
            for j in range(i + 1):
                tmp_sum = lsum[i] + msum[j]
                if tmp_sum > max_sum:
                    max_sum = tmp_sum

        return max_sum


s = Solution()
print(s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
print(s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
print(s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
print(s.maxSumTwoNoOverlap([2, 3, 1, 4], 1, 2))
