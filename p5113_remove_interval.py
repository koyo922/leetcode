#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[i] = [a, b] 都表示满足 a <= x < b 的所有实数  x 的集合。

我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。

返回删除所有交集区间后， intervals 剩余部分的 有序 列表。

 

示例 1：

输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
示例 2：

输入：intervals = [[0,5]], toBeRemoved = [2,3]
输出：[[0,2],[3,5]]
 

提示：

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/12/1 下午2:16
"""
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res, l, r = [], toBeRemoved[0], toBeRemoved[1]
        for a, b in intervals:
            if b <= l or a >= r:  # 待删除的区域完全在区段之外
                res.append((a, b))
                continue
            if l <= a <= b <= r:  # 待删除的区域完全包裹住该区段
                continue
            if l > a:  # 待删除左界大于区段左界
                res.append((a, l))
            if r < b:  # 待删除右界大于区段右界
                res.append((r, b))
        return res
