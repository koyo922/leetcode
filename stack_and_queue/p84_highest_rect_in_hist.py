#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/10 下午4:48
"""


class Solution:
    def mono_inc_stack(self, heights):
        res = 0
        stack = [(-1, 0)]  # 人为加个左开界
        for i, h in enumerate(heights + [0]):  # 加右边界
            while h < stack[-1][1]:
                # 先抛栈(比自己高的左侧柱), H记录被抛元素的高度
                H = stack.pop()[1]
                # 露出来的stack[-1][0]就是上一步被抛元素的左开界
                W = i - stack[-1][0] - 1
                # 用被抛元素为左闭界，i为右开界，更新最优解
                res = max(res, H * W)
            # push self
            stack.append((i, h))
        return res

    def count_higher_neighbors(self, heights):
        """
        left[i] := how many left(including self) `neighbors` which are higher/equal than heights[i]
        then bar[i] == heights[i] * (left[i] + right[i] - 1)
        """
        N = len(heights)
        if N == 0:
            return 0

        left, right = [1] * N, [1] * N
        for i, h in enumerate(heights):
            j = i - 1
            while j >= 0 and heights[j] >= h:
                left[i] += left[j]
                j -= left[j]  # 注意这里连跳了, 保证O(N)时间
        for i, h in reversed(tuple(enumerate(heights))):
            j = i + 1
            while j < N and heights[j] >= h:
                right[i] += right[j]
                j += right[j]
        return max(heights[i] * (left[i] + right[i] - 1) for i in range(N))

    def largestRectangleArea(self, heights):
        # return self.mono_inc_stack(heights)
        return self.count_higher_neighbors(heights)


if __name__ == '__main__':
    sol = Solution()
    assert 9 == sol.largestRectangleArea([5, 3, 5])
    assert 10 == sol.largestRectangleArea([2, 1, 5, 6, 2, 3])
