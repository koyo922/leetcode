#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/4 下午5:17
"""


class Solution:
    def inorder_recursive(self, root, k):
        # 中序遍历到第k个
        def mid_traverse(node):
            if node.left is not None:
                yield from mid_traverse(node.left)
            yield node.val
            if node.right is not None:
                yield from mid_traverse(node.right)

        for i, v in enumerate(mid_traverse(root), start=1):
            if i == k:
                return v

    def recurse_by_count(self, root, k):
        def count(node) -> int:
            if node is None:
                return 0
            return count(node.left) + count(node.right) + 1

        left_size = count(root.left)
        if left_size >= k:
            return self.recurse_by_count(root.left, k)
        elif left_size + 1 == k:
            return root.val
        else:
            return self.recurse_by_count(root.right, k - left_size - 1)

    def inorder_stack(self, root, k):
        # 中序遍历，用栈自己写（非递归）
        from collections import deque
        q = deque([])
        while k > 0:
            if root is not None:
                q.append(root)
                root = root.left
            else:
                t = q.pop()
                k -= 1
                if k == 0: return t.val
                root = t.right
        raise ValueError('k is invalid')

    def kthSmallest(self, root, k):
        return self.inorder_recursive(root, k)
        # return self.recurse_by_count(root, k)
        # return self.inorder_stack(root, k)
