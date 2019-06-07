#!/usr/bin/env python

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequentMap = {}
        for num in nums:
            frequentMap.setdefault(num, 0)
            frequentMap[num] += 1
        frequentList = [[] for _ in range(len(nums))]
        for num in frequentMap:
            frequent = frequentMap[num]
            frequentList[frequent - 1].append(num)
        total = 0
        resultList = []
        for frequent in range(len(nums), 0, -1):
            if not frequentList[frequent - 1]:
                continue
            numLen = len(frequentList[frequent - 1])
            if total + numLen < k:
                resultList.extend(frequentList[frequent - 1])
                total += numLen
            else:
                resultList.extend(frequentList[frequent - 1][0 : k - total])
                total = k
            if total >= k:
                break
        return resultList


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
