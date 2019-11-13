#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
题解: https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-san-chong-jie-by-chitan/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 上午10:21
"""
import collections
from typing import List


class Solution:
    def sort_and_merge(self, nums1: List[int], nums2: List[int]):
        intersection = []
        nums1.sort(), nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a < b:
                i += 1
            elif b < a:
                j += 1
            else:
                i, j = i + 1, j + 1
                intersection.append(a)
        return intersection

    def count_and_subtract(self, nums1: List[int], nums2: List[int]):
        intersection = []
        cnt = collections.Counter(nums1)
        for c in nums2:
            if cnt.get(c, 0) > 0:  # 注意检查的不是 "c in cnt"
                cnt[c] -= 1
                intersection.append(c)
        return intersection

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.sort_and_merge(nums1, nums2)
        # return self.count_and_subtract(nums1, nums2)
