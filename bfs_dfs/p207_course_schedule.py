#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/29 下午12:33
"""


class Solution:
    def naive_loop_seeds(self, numCourses, prerequisites):
        # 梳理依赖关系
        N = numCourses
        I, O = [set() for _ in range(N)], [set() for _ in range(N)]
        for cur, pre in prerequisites:
            I[cur].add(pre)
            O[pre].add(cur)
        # 逐个修完没有前序依赖的课程
        for _ in range(N):
            for cur, pres in enumerate(I):
                if pres == set():  # 且不是 None
                    # "修这门课"的方法就是:
                    I[cur] = None  # 1. 从I中抹去这门课
                    for post in O[cur]:  # 2. 将它从其后继课程的依赖关系中抹去
                        I[post].remove(cur)
                    break  # 找到了这种可以修的课程，就break出现找下一门
            else:  # 如果没有break，就是一门都没有找到，说明无解
                return False
        # 全部修完就是True
        return not any(I)

    def using_stack(self, numCourses, prerequisites):
        # 每次从头找入度为零的节点太慢；用stack/queue维护
        N = numCourses
        indegree = [0] * N  # 动态维护每门课的截至目前还有几门前序课程待修
        O = [set() for _ in range(N)]  # 下游关系
        for cur, pre in prerequisites:
            O[pre].add(cur)
            indegree[cur] += 1

        # 找出无依赖的种子课程
        n_done = 0
        stack = [n for n in range(N) if indegree[n] == 0]

        # 逐一修课；如果发现下游课程变成种子，也压入栈
        while stack:
            course = stack.pop()
            n_done += 1
            for post in O[course]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    stack.append(post)

        # 栈空之后无法继续排课；此时如果修完了，就是 canFinish
        return n_done == N

    def using_dfs(self, numCourses, prerequisites):
        N = numCourses
        # 节点未访问置0，正在被访问置-1，访问过了置1
        visit = [0] * N

        # 梳理下游关系
        O = [set() for _ in range(N)]
        for cur, pre in prerequisites:
            O[pre].add(cur)

        def dfs(i):
            if visit[i] == -1:  # 撞到了正在遍历路径上的节点，有环
                return False
            if visit[i] == 1:  # 该节点已经遍历且返回过，多条上游汇合
                return True
            visit[i] = -1  # pre
            if any(not dfs(j) for j in O[i]):
                return False
            visit[i] = 1  # post
            return True

        # 从任意点出发都不能遇到环
        return all(dfs(i) for i in range(N))

    def canFinish(self, numCourses, prerequisites):
        # return self.naive_loop_seeds(numCourses, prerequisites)
        # return self.using_dfs(numCourses, prerequisites)
        return self.using_stack(numCourses, prerequisites)


if __name__ == '__main__':
    print(Solution().canFinish(2, [(1, 0)]))
    print(Solution().canFinish(2, [(1, 0), (0, 1)]))
