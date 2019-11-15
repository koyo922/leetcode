#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/15 下午6:22
"""


class Solution:
    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return res

        imin, imax, jmin, jmax = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while imin <= imax and jmin <= jmax:
            res += matrix[imin][jmin:jmax + 1]  # 西北->东北 (前闭后闭)
            res += (matrix[i][jmax] for i in range(imin + 1, imax + 1))  # 东北->东南 (前开后闭)
            if imin < imax and jmin < jmax:  # 退化成横/竖线之后，不必再重复考虑西南两边了
                for j in range(jmax - 1, jmin, -1):  # 东南->西南 (前开后开)
                    res.append(matrix[imax][j])  # 注意逆序

                for i in range(imax, imin, -1):  # 西南->西北 (前闭后开)
                    res.append(matrix[i][imin])
            # 收紧一圈
            imin, jmin = imin + 1, jmin + 1
            imax, jmax = imax - 1, jmax - 1

        return res
