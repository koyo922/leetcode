#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/24 下午7:04
"""


class Solution:
    def partition(self, s):
        N = len(s)
        # p[i][j] := 子串s[i~j]是否回文
        # p[i][j] = p[i+1][j-1] && s[i]==s[j]
        p = [[False] * N for _ in range(N)]

        # 定义res[j-1] 表示 s[0~(j-1)] 这段子串的所有对称拆分方案
        # 如果 s[j~i] 是回文的（即p[j][i]==True）
        # 则可使用 s[j~i]这个回文片段，来扩展res[j-1]中已有的各个拆分方案，扩充长度到i
        res = [[] for _ in range(N)]
        for i in range(N):
            # 注意是在 res[j-1]的基础上扩充 s[j~i]; 所以j最大可以取到i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or p[j + 1][i - 1]):
                    p[j][i] = True
                    if j == 0:  # 此时 res[j-1]还不存在，需要人为定义一个 "res[:0]"
                        res[i] += [[s[j:i + 1]]]
                        # 相当于 res[i] += [sol + [s[j:i + 1]] for sol in [[]]]
                    else:
                        res[i] += [sol + [s[j:i + 1]] for sol in res[j - 1]]
        return res[-1]
