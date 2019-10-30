#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/7/7 下午8:46
"""

from __future__ import division


class Solution(object):
    def brute_force(self, x, n):
        return x ** n

    def recursive(self, x, n):
        if n < 0:  # 先考虑负次幂
            return 1 / self.myPow(x, -n)
        if n in (0, 1):
            return x ** n
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)  # x*x 比 x**2稳；后者偶尔溢出
        else:
            return self.myPow(x, n - 1) * x

    def iterative(self, x, n):
        if n < 0:
            x, n = 1 / x, -n
        power = 1  # 最后累计的积
        while n:  # 对于二进制的n，从右往左取位
            if n & 1:
                power *= x
            x *= x  # 每次x都对自己平方；依次变为 x, x^2, x^4, x^8 ...
            n >>= 1  # 下次取n的左边一位
        return power
