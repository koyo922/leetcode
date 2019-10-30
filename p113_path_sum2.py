#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/23 上午11:49
"""


class Solution:

    def naive_dfs(self, root, sum):
        def dfs(node, S, path):
            curS = S + node.val
            curP = path + [node.val]
            # if curS > sum: # might contain negative values
            #     return
            if node.left:
                dfs(node.left, curS, curP)
            if node.right:
                dfs(node.right, curS, curP)
            if not node.left and not node.right and curS == sum:
                res.append(curP)

        res = []
        if root:
            dfs(root, 0, [])
        return res

    def dfs_clean(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]  # CAUTION double [[]]
        return [([root.val] + p) for p in
                (self.dfs_clean(root.left, sum - root.val) +
                 self.dfs_clean(root.right, sum - root.val))]

    def bfs(self, root, sum):
        if not root:
            return []
        res = []
        from collections import deque
        q = deque([(root, root.val, [root.val])])
        while q:
            node, val, path = q.popleft()
            if not node.left and not node.right and val == sum:
                res.append(path)
            if node.left:
                q.append((node.left, val + node.left.val, path + [node.left.val]))
            if node.right:
                q.append((node.right, val + node.right.val, path + [node.right.val]))
        return res

    def pathSum(self, root, sum):
        return self.naive_dfs(root, sum)
        # return self.dfs_clean(root, sum)
        # return self.bfs(root, sum)
