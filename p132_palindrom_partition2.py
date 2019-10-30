#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/24 下午7:34
"""


class Solution:
    def minCut(self, s):
        N = len(s)
        p = [[False] * N for _ in range(N)]
        dp = [0] * N

        for i in range(N):
            # 前i个字符构成的子串，最优需要m刀
            m = i  # 最差也就i-1刀切成每字独立，但是要避免i=0时的 -1
            # j是遍历尝试的切点，分成两段 0~j 和 j+1~i-1
            # 左段最优刀数 dp[j-1]，右端如果对称的话就是0刀，左右之间有一刀，总共 dp[j-1]+1 刀
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or p[j + 1][i - 1]):
                    p[j][i] = True
                    m = 0 if j == 0 else min(m, dp[j - 1] + 1)
            dp[i] = m
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minCut('ab'))
