#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/4 下午5:45
"""

from functools import lru_cache


class Solution:

    def naive_dfs(self, input):
        # 沿着运算符，左右递归
        @lru_cache()
        def dfs(expression):
            res = []  # CAUTION  {} is literal DICT, not SET
            for i, op in enumerate(expression):
                if op not in '+-*':
                    continue
                # 沿着运算符op切开，左右分别算可能的值
                L = dfs(expression[:i])
                R = dfs(expression[i + 1:])
                # 结合运算符，得到结果；扩充res
                res.extend([eval('{}{}{}'.format(l, op, r)) for l in L for r in R])
            # 如果res为空说明expression中就没有运算符，是个scalar
            return res or [eval(expression)]

        return dfs(input)

    @lru_cache()
    def clean_dfs(self, input):
        # https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66350/1-11-lines-Python-9-lines-C++
        return [eval('{}{}{}'.format(a, op, b))
                for i, op in enumerate(input) if op in '+-*'
                for a in self.clean_dfs(input[:i])
                for b in self.clean_dfs(input[i + 1:])
                ] or [eval(input)]

    def using_dp(self, input):
        # 有了recursion+LRU_cache之后，其实DP没太大必要了
        # https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66331/C++-4ms-Recursive-and-DP-solution-with-brief-explanation
        pass

    def diffWaysToCompute(self, input):
        return self.naive_dfs(input)
        # return self.clean_dfs(input)


if __name__ == '__main__':
    print(Solution().diffWaysToCompute('2-1-1'))
    print(Solution().diffWaysToCompute('2*3-4*5'))
