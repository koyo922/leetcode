#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/13 下午9:16
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        # return self.subset_sum(nums, s // 2, style='dfs')
        return self.subset_sum(nums, s // 2, style='ransack')

    def subset_sum(self, nums, s, style='dfs'):
        if style == 'dfs':
            dp = [True] + [False] * s
            for n in nums:
                # 尝试用n去对 大于等于自己的状态做扩充
                for i in range(s, n - 1, -1):  # 注意步长为1，且倒拖地
                    dp[i] |= dp[i - n]
                if dp[s]: return True
            return dp[s]
        elif style == 'ransack':
            dp = [0] * (s + 1)  # 背包方法的存储量更大，比上述深搜更慢
            # 01背包问题原始转移方程 f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}
            # 可以写成如下 rolling写法，注意j要倒拖地
            for n in nums:
                for j in range(s, n - 1, -1):
                    dp[j] = max(dp[j], dp[j - n] + n)
            return dp[s] == s
        else:
            raise NotImplementedError(style)
