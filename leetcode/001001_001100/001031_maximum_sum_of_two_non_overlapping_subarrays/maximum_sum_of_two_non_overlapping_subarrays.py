#!/usr/bin/env python

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, a: List[int], l: int, m: int) -> int:
        """

        define asum[i] as the sum of subarray, a[0:i]
        define maxl[i] as the maximum sum of l-length subarray in a[0:i]
        define maxm[i] as the maximum sum of m-length subarray in a[0:i]
        define msum[i] as the maximum sum of non-overlap l-length subarray and m-length subarray

        case 1: a[i] is both not in l-length subarray and m-length subarray, then msum[i] = msum[i - 1]
        case 2: a[i] is in l-length subarray, then msum[i] = asum[i] - asum[i-l] + maxm[i-l]
        case 3: a[i] is in m-length subarray, then msum[i] = asum[i] - asum[i-m] + maxl[i-m]

        so, msum[i] = max(msum[i - 1], asum[i] - asum[i-l] + maxl[i-l], asum[i] - asum[i-m] + maxm[i-m])
        """

        alen, tlen = len(a), l + m
        asum = [0] * (alen + 1)
        maxl = [0] * (alen + 1)
        maxm = [0] * (alen + 1)
        msum = [0] * (alen + 1)

        for i in range(tlen):
            if i == 1:
                asum[i] = a[i - 1]
            elif i > 1:
                asum[i] = asum[i - 1] + a[i - 1]
            if i >= l:
                maxl[i] = max(maxl[i - 1], asum[i] - asum[i - l])
            if i >= m:
                maxm[i] = max(maxm[i - 1], asum[i] - asum[i - m])

        for i in range(tlen, alen + 1):
            asum[i] = asum[i - 1] + a[i - 1]
            suml = asum[i] - asum[i - l]
            summ = asum[i] - asum[i - m]
            maxl[i] = max(maxl[i - 1], suml)
            maxm[i] = max(maxm[i - 1], summ)
            msum[i] = max(msum[i - 1], suml + maxm[i - l], summ + maxl[i - m])

        return msum[-1]


s = Solution()
print(s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
print(s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
print(s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
print(s.maxSumTwoNoOverlap([2, 3, 1, 4], 1, 2))
