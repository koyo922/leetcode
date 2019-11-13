#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 下午8:09
"""
from definitions import TreeNode


class Solution:
    def recursive(self, root):
        def is_mirror(l, r):
            if l is None and r is None:  # 同为None 是对称
                return True
            if l is None or r is None:  # 仅一边为None  非对称
                return False
            # 两边都非None 递归
            return l.val == r.val and is_mirror(l.right, r.left) and is_mirror(l.left, r.right)

        return is_mirror(root.left, root.right) if root else True

    def iterative(self, root: TreeNode) -> bool:
        if root is None:
            return True  # 注意边界值
        s = [(root.left, root.right)]  # 注意tuple
        while s:
            t1, t2 = s.pop()
            # 两个节点都为空, 则继续判断
            if not t1 and not t2: continue
            # 存在一个节点为空, 则为False
            if not (t1 and t2): return False
            if t1.val != t2.val: return False
            # t1, t2的左右节点, 要对称的写入双端队列中
            s.append((t1.left, t2.right))
            s.append((t1.right, t2.left))
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.recursive(root)
        # return self.iterative(root)
