#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/29 下午12:15
"""


class Solution:
    def naive_dp(self, nums):
        """
        sol1: mine DP
        dp[i]:= max possible income by ending(including) with nums[i]
        dp[0], dp[1] = nums[0], nums[1]
        dp[i] = max(dp[:i-1]+nums[i])
              = max(dp[i-3],dp[i-2])+nums[i]
        """
        # N<4的边界情况
        N = len(nums)
        if N == 0:
            return 0
        elif N <= 2:
            return max(nums)
        elif N == 3:
            return max(nums[0] + nums[2], nums[1])
        # 定义N>=4时的初始状态
        a, b, c, d = nums[:4]
        dp = [a, b, a + c, max(a, b) + d]
        # 开始DP
        for i in range(4, N):
            dp.append(max(dp[i - 3:i - 1]) + nums[i])
        return max(dp[-2:])

    def rolling_dp(self, nums):
        """
        sol2: raw DP definition with rolling array, O(1) space
        直接定义dp[i]为原问题：nums[:i]对应的解；递推关系反而更简单
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        """
        pre, cur = 0, 0  # 注意定义dp[-2],dp[-1]的技巧避免特殊case
        for n in nums:
            pre, cur = cur, max(pre + n, cur)
        return cur

    def rob(self, nums):
        return self.naive_dp(nums)
        # return self.rolling_dp(nums)
