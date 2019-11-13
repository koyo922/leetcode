#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 下午5:27
"""


class Solution:
    def recurse_diameter_and_depth(self, root):
        """
        如果不经过根，则分别递归到左/右子树
        否则，就是 左子树的深度+1+右深度+1
        """

        def dep_and_diam(node):
            """后根遍历，先求出左右子树的深度和直径"""
            if node is None:
                return 0, 0
            left_depth, left_diameter = dep_and_diam(node.left)
            right_depth, right_diameter = dep_and_diam(node.right)
            # 注意如果左子树为None，算直径时就不能接续上 left_depth + 1
            to_left_depth = left_depth + 1 if node.left else 0
            to_right_depth = right_depth + 1 if node.right else 0
            return (max(to_left_depth, to_right_depth),
                    max(left_diameter, right_diameter,
                        to_left_depth + to_right_depth))

        return dep_and_diam(root)[1]

    def post_traversal(self, root):
        """
        后根遍历，自然会由低到高
        最优解不一定会穿过root节点，但是它必然穿过某个子树的根
        我们对所有的节点都当作根遍历，一定能考虑到最优解

        问题被简化成，求穿过node节点的node子树的直径
        diameter = max(left_depth, right_depth) + 1
        注意，这里只用到depth的概念(无论左右是否为空，深度总是要加1的)
        不涉及直径,递归更好写

        另外：可能像下面这样想，来自然引出简洁解法:
        上面用到了两处max,第二处的max就是在比较直径；
        这个操作比较转化为全局的比较
        """
        max_diameter = 0

        def depth(node):
            nonlocal max_diameter
            if node is None:
                return 0
            l_depth, r_depth = depth(node.left), depth(node.right)
            # 更新最优直径
            diameter_past_me = l_depth + r_depth
            max_diameter = max(max_diameter, diameter_past_me)
            # 自己的深度
            my_depth = max(l_depth, r_depth) + 1
            return my_depth

        depth(root)  # 记得要先调用一遍，触发计算
        return max_diameter

    def diameterOfBinaryTree(self, root):
        return self.recurse_diameter_and_depth(root)
        # return self.post_traversal(root)
