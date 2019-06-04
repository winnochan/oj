#!/usr/bin/env python


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mlen = 0
        slen = len(s)
        dp = [0] * (slen + 1)
        for i in range(1, len(s) + 1):
            # 有效的括号对不可能会以'('结尾的
            if s[i - 1] == '(':
                continue

            left_paren = i - 2 - dp[i - 1]
            if left_paren >= 0 and s[left_paren] == '(':
                dp[i] = dp[i - 1] + 2

                # 拼接有效括号对
                if dp[i - dp[i]]:
                    dp[i] += dp[i - dp[i]]

                # 更新最大有效扩对长度
                if dp[i] > mlen:
                    mlen = dp[i]

        return mlen


s = Solution()
print(s.longestValidParentheses('(())())'))
