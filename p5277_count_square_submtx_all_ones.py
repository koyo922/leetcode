#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

 

示例 1：

输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释：
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.
示例 2：

输入：matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
 

提示：

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/jian-dan-qing-xi-de-yuan-di-dong-tai-gui-hua-java-/

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/12/1 下午1:31
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        就地改动 matrix[i][j] := 坐标(i,j)左侧连续1的个数
        以(i,j)为右下角，注意题意只考虑"正方形"; 显然，合法的正方形变长不会超过重新定义的matrix[i][j], 记作maxlen
        就将j逐步上移，即 从正方形的东南角出发，不断抬高东北角
        沿途记录所见过的minlen(不断收紧), 以及逐渐变长的curlen(不断扩张)
        直到 curlen > maxlen or minlen < curlen or row < 0
        """
        res = 0
        for i in range(len(matrix)):
            for j, c in enumerate(matrix[i]):
                if c != 1: continue
                res += 1
                if j == 0:
                    matrix[i][j] = 1
                    continue
                matrix[i][j] = matrix[i][j - 1] + 1

                if i == 0: continue
                minlen = maxlen = matrix[i][j]
                row, curlen = i - 1, 2
                while row >= 0 and curlen <= maxlen:
                    minlen = min(minlen, matrix[row][j])
                    if minlen < curlen: break
                    res += 1
                    row -= 1
                    curlen += 1
        return res
