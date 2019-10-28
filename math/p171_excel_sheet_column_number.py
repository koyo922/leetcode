#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
致谢：
特别感谢 @ts 添加此问题并创建所有测试用例。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/28 下午3:15
"""


class Solution:
    def naive_power(self, s):
        res = 0
        for i, c in enumerate(s[::-1]):
            res += (ord(c) - ord('A') + 1) * (26 ** i)
        return res

    def shift_prefix(self, s):
        """
        也可以从高到低写，不用做指数运算，更快
        注意技巧：连续的连乘可以用类似前缀的方式写，不必每次从头开始乘
        """
        res = 0
        ordA = ord('A')
        for c in s:
            res *= 26  # 前缀式的连乘
            res += ord(c) - ordA + 1
        return res

    def titleToNumber(self, s):
        return self.naive_power(s)
        # return self.shift_prefix(s)
