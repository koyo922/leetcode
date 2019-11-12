#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/4 下午6:43
"""


class Solution:
    def literal(self, num):
        # 定义好"字面和"函数，反复调用即可
        def digit_sum(n):
            res = n % 10
            while n >= 10:
                n //= 10
                res += n % 10
            return res

        while num >= 10:
            num = digit_sum(num)
        return num

    def double_loop(self, num):
        # 同上，但是没必要写函数，可以直接用双层循环

        while num >= 10:  # 一直处理到num为个位数为止
            temp_sum = 0
            while num > 0:  # 逐位求和num，不用保留num原值，所以放心修改
                temp_sum += num % 10
                num //= 10
            num = temp_sum
        return num

    def number_theory(self, num):
        """
        这个问题就是数论中的Digital Root问题,有O(1)时间解
        假设a[0]表示num, a[1]表示a[0]的字面和, a[2]表示a[1]的字面串...
        a[n]表示a[n-1]的字面和（最后一个数 0<a[n]<=9）
        分析一下a这个数列的规律：
        设num为'ABCD',即 1000A + 100B + 10C + 1D
        有   (1000A+100B+10C+1D) % (10-1)
        =   (A+999A + B+99B + C+9C + D) % 9
        =   (A+B+C)%9 + (999A+99B+9C)%9
        =   (A+B+C)%9
        对应到数列a的递推式就是：
            num%9
        =   a[0]%9 (定义a[0]==num)
        =   a[1]%9
        =   a[2]%9
        =   ...
        =   a[n]%9， （a[n]就是最终要求的数；根据定义,0<a[n]<=9，对9取模大致还是自己）
        =   a[n] if a[n]%9!=0 else 9
        有一个特殊情况就是num==0时，直接返回0
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9

    def addDigits(self, num):
        return self.literal(num)
        # return self.double_loop(num)
        # return self.number_theory(num)
