#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

 

示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 上午11:28
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        i, j = 0, len(A) - 1
        for _ in range(len(A)):
            a, b = A[i] ** 2, A[j] ** 2
            if a > b:
                res.append(a)
                i += 1
            else:
                res.append(b)
                j -= 1
        return res[::-1]
