#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 

注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/13 下午9:57
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0 or max(nums) > s // k:
            return False

        used = [False] * len(nums)  # 每个数的占用状态

        def dfs(remaining_rnd, target, accum, start):
            if remaining_rnd == 0:
                return True
            if accum == target:  # 完成当前轮次积累
                return dfs(remaining_rnd - 1, target, 0, 0)
            for i in range(start, len(nums)):
                # 如果当前位使用后不越界，就尝试深搜下去; 注意可用区间是轮次内是单调的
                if (not used[i]) and accum + nums[i] <= target:
                    used[i] = True
                    if dfs(remaining_rnd, target, accum + nums[i], i + 1): return True
                    used[i] = False
            return False

        return dfs(k, s // k, 0, 0)
