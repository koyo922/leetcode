#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

 

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

说明:

骑士的健康点数没有上限。

任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dungeon-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/28 下午3:20
"""


class Solution:
    def naive_dp(self, dungeon):
        """
        sol1: DP, choose the safest path
        http://leetcodesolution.blogspot.kr/2015/01/leetcode-dungeon-game.html
        minInitHealth[i][j] = min(minInitHealth[i+1][j], minInitHealth[i][j+1]) - dungeon[i][j]
        set minInitHealth[i][j] to 1 if < 1
        """
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0] * N for _ in range(M)]
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                # choose right/down, whichever requires less
                if i == M - 1 and j == N - 1:
                    base = 1
                elif i == M - 1:
                    base = dp[i][j + 1]
                elif j == N - 1:
                    base = dp[i + 1][j]
                else:
                    base = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, base - dungeon[i][j])  # always ensure >= 1
        return dp[0][0]

    def rolling_dp(self, dungeon):
        # 在dp矩阵底部添加一行，tricky
        need = [float('inf')] * (len(dungeon[0]) - 1) + [1]
        for row in reversed(dungeon):
            # enumerate不是sequence，无法直接套用reversed()
            for j, v in reversed(tuple(enumerate(row))):
                # 注意python切片语法的右界可以溢出(j+1越界没关系)，简化语法
                need[j] = max(1, min(need[j:j + 2]) - v)
        return need[0]

    def calculateMinimumHP(self, dungeon):
        # return self.naive_dp(dungeon)
        return self.rolling_dp(dungeon)
