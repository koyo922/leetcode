#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/additive-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/13 下午10:18
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        style = 'iterative'

        def is_valid(a, b, remaining):
            if style == 'recursive':
                if not remaining: return True
                a, b = b, str(int(a) + int(b))
                return remaining.startswith(b) and is_valid(a, b, remaining[len(b):])
            else:
                assert style == 'iterative'
                while remaining:
                    a, b = b, str(int(a) + int(b))
                    if not remaining.startswith(b): return False
                    remaining = remaining[len(b):]  # str 类型不支持 del arr[:3] 这样的操作
                return True

        N = len(num)
        for i in range(1, N // 2 + 1):
            L = num[:i]
            if num[0] == '0' and len(L) > 1: return False
            for j in range(i + 1, N):
                R = num[i:j]
                if N - j < max(len(L), len(R)): break  # 剩余长度短于 L或者R
                if R[0] == '0' and len(R) > 1: break
                if is_valid(L, R, num[j:]): return True
        return False
