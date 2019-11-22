#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式

该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。

你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

示例 1:

输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

输出: [1]
示例 2:

输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

输出: [3, 4]
说明:

 根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
树的高度是指根节点和叶子节点之间最长向下路径上边的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/22 上午10:58
"""

from collections import defaultdict


class Solution:

    def middle_of_diameter(self, _n, edges):
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # DFS(pre-order) 迭代式; 递归可能栈溢出
        def dfs_longest_path(v):
            stack, visited = [(v, 0)], {v}
            path, longest_path, max_len = [], None, -1
            while stack:
                node, level = stack.pop()
                path = path[:level] + [node]
                if level > max_len:
                    max_len = level
                    longest_path = path
                for n in adj[node] - visited:
                    stack.append((n, level + 1))
                    visited.add(n)
            return longest_path

        p0_A = dfs_longest_path(0)  # 从0号节点出发的一条最长路径; 其终点必然是个偏僻点
        D = dfs_longest_path(p0_A[-1])  # 从该偏僻点出发的最长路径; 必然就是直径
        M = len(D)  # 直径长度若为奇数，根只有一个; 否则中间两个节点都可以
        return D[(M - 1) // 2: M // 2 + 1]

    def stripe_leaves(self, n, edges):
        """ 逐层剥离叶子，直到剩最后1~2个点 """
        if n == 1: return [0]
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()  # i既然是leaf，j就是i唯一的邻居
                adj[j].remove(i)  # 该邻居又少了一个邻接点
                # 新叶子只可能是当前叶子的邻居, 限定范围加速
                if len(adj[j]) == 1: new_leaves.append(j)
            leaves = new_leaves
        return leaves

    def findMinHeightTrees(self, n, edges):
        return self.middle_of_diameter(n, edges)
        # return self.stripe_leaves(n, edges)
