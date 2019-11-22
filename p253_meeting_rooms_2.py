#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
题目描述
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],…] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

tag
贪心 堆

样例
1
2
输入: [[0, 30],[5, 10],[15, 20]]
输出: 2

http://shaocheng.me/2019/07/18/LeetCode-253-Meeting-Rooms-II/

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/20 上午7:44
"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """ 小顶堆贪心，取最早结束的会议室 """
        if not intervals:
            return 0

        free_rooms = []  # 准备好会议室资源堆, 元素是各场会议的结束时间
        intervals.sort(key=lambda x: x[0])  # 按照开始时间排序

        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:  # 如果堆顶(最早的前序会议结束时间)小于本会议的开始时间
                heapq.heappop(free_rooms)  # 说明最早空出来的那间已经可用, 抛出&复用，节省会议室
            heapq.heappush(free_rooms, i[1])  # 将本会议入堆
        return len(free_rooms)  # 注意全程会议室资源都是单调递增的
