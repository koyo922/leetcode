#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/29 下午12:27
"""

from definitions import TreeNode


class Solution:
    def bfs(self, root):
        res = []
        q = [root] if root else []
        while q:
            res.append(q[-1].val)  # CAUTION
            q = [k for n in q for k in (n.left, n.right) if k]
        return res

    def dfs(self, root):
        rightmost_value_at_depth = []
        stack = [(root, 0)]  # tuple<node, depth>
        while stack:
            node, depth = stack.pop()
            if node:
                # 利用栈的性质，每个新层都是尽可能靠右的首次到达
                if depth >= len(rightmost_value_at_depth):
                    rightmost_value_at_depth.append(node.val)
                # 注意right后进先出；抛栈的时候才改记录；所以结果是尽量靠右
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return rightmost_value_at_depth

    def rightSideView(self, root):
        # return self.bfs(root)
        return self.dfs(root)


if __name__ == '__main__':
    res = Solution().rightSideView(TreeNode(1))
    print(res)
