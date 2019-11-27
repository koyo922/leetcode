#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

https://leetcode-cn.com/problems/unique-binary-search-trees/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-8/


Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/27 上午10:44
"""


class Solution:
    def using_recur(self, n: int) -> int:
        import functools
        @functools.lru_cache(None)
        def recur(m):
            if m < 2: return 1
            return sum(recur(i) * recur(m - i - 1) for i in range(m))

        return recur(n)

    def dp(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for j in range(2, n + 1):
            G[j] = sum(G[i] * G[j - i - 1] for i in range(j))
        return G[n]

    def using_catalan(self, n: int) -> int:
        C = 1
        for i in range(n):  # 这里不能换成 整数除`//` 或者 下面去掉 `int()`
            C *= 2 * (2 * i + 1) / (i + 2)
        return int(C)

    def numTrees(self, n: int) -> int:
        # return self.using_recur(n)
        return self.dp(n)
        # return self.using_catalan(n)
