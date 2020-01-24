#!/usr/bin/env python


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        定义dp[i]为以s[i]字符结尾的最长回文长度

        #a#b#b#a
        定义dp[i]为以s[i]为中心的回文字串半径, 则dp[i] = ;
        '''

        # 空字符串
        if not len(s):
            return ''

        # 去除偶回文
        s = '#' + '#'.join(list(s)) + '#'
        slen = len(s)

        dp = [0] * slen
        dp[0] = 1

        maxi = 0
        for i in range(1, slen):
            left = i - 1 - dp[i - 1]
            if left < 0 or s[left] != s[i]:
                if s[i] == s[left + 2]:
                    dp[i] = i - left - 1
                else:
                    dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 2

            if dp[i] > dp[maxi]:
                maxi = i
            elif dp[i] == dp[maxi] and s[maxi] == '#' and s[i] != '#':
                maxi = i

        plen = (dp[maxi] + 1) // 2 if s[maxi] != '#' else (dp[maxi] - 1) // 2
        bi = maxi // 2 - plen + 1

        print(list(s))
        print([str(i) for i in dp])

        return o[bi:bi + plen]


s = Solution()
print(s.longestPalindrome("bananas"))
