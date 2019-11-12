#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/4 下午5:03
"""


class Solution:
    def using_stack(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():  # 把当前的数字读完，取sign，加到total上
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                # 注意缩进 indent
                total += signs.pop() * int(s[start:i])
                continue  # avoid more i+=1
            if c in '+-(':  # 压合适的sign入栈
                # 注意逗号不可省，是tuple；否则不能直接 list += int
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':  # 抛符号栈
                signs.pop()
            i += 1
        return total

    def using_dfs(self, s):
        def dfs():
            nonlocal i, N
            res, sign, num = 0, 1, 0
            while i < N and s[i] != ')':
                c = s[i]
                if c.isdigit():
                    # 注意+= 是9，=才是10倍
                    num += num * 9 + int(c)
                else:
                    res += sign * num
                    num = 0
                    if c == '+':
                        sign = 1
                    elif c == '-':
                        sign = -1
                    elif c == '(':
                        i += 1
                        res += sign * dfs()
                i += 1
            return res + sign * num

        i, N = 0, len(s)
        return dfs()

    def calculate(self, s):
        return self.using_stack(s)
        # return self.using_dfs(s)


if __name__ == '__main__':
    # print(Solution().calculate("1 + 1"))
    # print(Solution().calculate(" 2-1 + 2 "))
    print(Solution().calculate("2147483647"))
