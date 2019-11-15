#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/15 下午4:57
"""
from typing import List


class Solution:
    def dp(self, height: List[int]) -> int:
        """ 前缀和 & 后缀和 分别累计 max_left / max_right; O(2N)空间 """
        N = len(height)
        left_max, right_max = [0] * N, [0] * N
        # 统计左侧最高边界
        left_max[0] = height[0]
        for i in range(1, N):
            left_max[i] = max(left_max[i - 1], height[i])
        # 统计右侧最高边界
        right_max[-1] = height[-1]
        for i in range(N - 2, -1, -1):  # 注意最后step=-1
            right_max[i] = max(right_max[i + 1], height[i])
        # 累加每根竖向水柱, 注意i的范围不包含左右两端
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(1, N - 1))

    def mono_stack(self, height: List[int]) -> int:
        """ 单调下降栈；遇到高于栈顶，就弹出并累计雨水; 在完全单调case中，占用O(n)空间 """
        res, s = 0, []
        for i, h in enumerate(height):
            while s and h > s[-1][1]:  # 高于栈顶, 注意是 s[-1][1] 记得取高度
                top_idx, top_height = s.pop()  # 弹出栈顶元素(下标)，露出来的是它的左界下标
                if not s:
                    break
                distance = i - s[-1][0] - 1  # 左右界距离
                bounded_height = min(h, s[-1][1]) - top_height
                res += distance * bounded_height
            s.append((i, h))
        return res

    def double_pointers(self, height: List[int]) -> int:
        """ 左右夹逼，较低的一边动；同时记录scalar的left_max/right_max水位; O(1)空间 """
        res, l, r = 0, 0, len(height) - 1
        l_max, r_max = 0, 0
        while l < r:  # 直到左右指针相遇
            if height[l] < height[r]:  # 如果左指针比较低
                if height[l] > l_max:  # 如果高于之前的边界
                    l_max = height[l]  # 更新边界
                else:  # 否则, 从两侧海岸边一路推过来，一定能包住当前位置
                    res += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    res += r_max - height[r]
                r -= 1
        return res

    def trap(self, height: List[int]) -> int:
        if height is None or len(height) < 2:
            return 0
        return self.dp(height)
        # return self.mono_stack(height)
        # return self.double_pointers(height)
