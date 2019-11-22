#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/22 上午11:35
"""


class Solution:
    def maxCoins(self, nums):
        # 左右界加[1]方便统一处理；去掉中间的0，因为不产生coin
        nums = [1] + [i for i in nums if i > 0] + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        # 逆向思考，考虑最后一个爆的气球；左右都已知了
        for k in range(2, N):  # 子区间长度
            for left in range(N - k):
                right = left + k  # 给定左界确定右界
                # 从 left+1 ~ right-1 尝试最后爆炸点; 短于k的dp区段前面已经解决过了，直接读取
                dp[left][right] = max(dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right]
                                      for i in range(left + 1, right))
        return dp[0][N - 1]  # O(n^3)


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
