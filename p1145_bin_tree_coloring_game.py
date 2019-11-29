#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。

 

游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，

「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；

「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。

「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。

 

之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。

如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

 

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。

 

示例：



输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：True
解释：第二个玩家可以选择值为 2 的节点。
 

提示：

二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。
n 为奇数。
1 <= x <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-coloring-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

https://leetcode-cn.com/problems/binary-tree-coloring-game/solution/shen-du-you-xian-sou-suo-python3-by-smoon1989-3/

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/29 下午3:35
"""

from definitions import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, _n: int, x: int) -> bool:
        """
        将二叉树视为图, 张三的首个落点将图分为3个连通分量
        按照规定只能邻接生长, 所以李四在root的左、右、上三个连通分量中挑最重的一个; 同时也把自己关进这个分量中
        然后张三可以独占另外的两个分量
        因此; 关键逻辑是： 如果最初产生的3个分量中存在任何一方重量超过全树一半的，则李四必胜；否则必败
        """
        L, R = 0, 0  # 张三落点左右方向的连通分量的重量

        def size(node):  # 某个节点对应的子树重量
            if node is None: return 0
            left, right = size(node.left), size(node.right)
            if node.val == x:  # 遭遇张三首落点时，顺便更新L, R
                nonlocal L, R
                L, R = left, right
            return left + right + 1

        n = size(root)  # _n参数其实没必要
        return any(p > n // 2 for p in (L, R, n - L - R - 1))
