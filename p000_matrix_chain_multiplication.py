#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
问题描述
在计算矩阵连乘积时，加括号的方式对计算量有影响。

例如有三个矩阵A1,A2,A3连乘，它们的维数分别为
10×100,100×5,5×50。用第一种加括号方式(A1A2)A3计算，则所需数乘次数为10×100×5+10×5×50=7,500。
用第二种加括号方式A1(A2A3)计算，需要100×5×50+10×100×50=75,000次数乘。

输入连乘矩阵的个数，每个矩阵的维数。要求输出数乘次数最少时的加括号方式，及数乘次数。

- https://w8ed.me/2019/01/28/%E5%88%B7%E9%A2%98%20%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E2%80%94%E2%80%94%E7%9F%A9%E9%98%B5%E8%BF%9E%E4%B9%98%E9%97%AE%E9%A2%98/
- https://www.cnblogs.com/mozi-song/p/9629137.html
- https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_B

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/22 下午1:21
"""
import sys


def main():
    f = sys.stdin
    n = int(f.readline())
    row, col = [0] * n, [0] * n
    for i in range(n):
        row[i], col[i] = map(int, f.readline().split())

    INF = float('inf')
    dp = [[INF] * n] * n
    for i in range(n - 1, -1, -1):  # 注意i降j升, 以便保障依赖的内部dp都已经处理过
        for j in range(i, n):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + row[i] * col[j] * col[k] for k in range(i, j))
    print(dp[0][-1])  # 注意不是return


if __name__ == '__main__':
    main()
