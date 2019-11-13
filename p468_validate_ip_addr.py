#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。

示例 1:

输入: "172.16.254.1"

输出: "IPv4"

解释: 这是一个有效的 IPv4 地址, 所以返回 "IPv4"。
示例 2:

输入: "2001:0db8:85a3:0:0:8A2E:0370:7334"

输出: "IPv6"

解释: 这是一个有效的 IPv6 地址, 所以返回 "IPv6"。
示例 3:

输入: "256.256.256.256"

输出: "Neither"

解释: 这个地址既不是 IPv4 也不是 IPv6 地址。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 下午8:45
"""


class Solution:
    def rule_match(self, IP: str) -> str:
        p = IP.split('.')
        if len(p) == 4:
            for r in p:
                if not 1 <= len(r) <= 3:
                    return 'Neither'  # 位数不对
                if len(r) >= 2:
                    if not ('1' <= r[0] <= '9'):
                        return 'Neither'  # 首位有其他值
                if not all('0' <= c <= '9' for c in r):
                    return 'Neither'  # 有非数字
                if int(r) > 255:
                    return 'Neither'  # 大于255
            return 'IPv4'

        p = IP.split(':')
        if len(p) == 8:
            for r in p:
                if not 1 <= len(r) <= 4:
                    return 'Neither'  # 位数不对
                if not all(('0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F') for c in r):
                    return 'Neither'  # 有非数字
            return 'IPv6'

        return 'Neither'

    def using_regex(self, IP: str) -> str:
        import re
        # 注意结尾补点方便; fullmatch
        if (re.fullmatch(r"(([1-9]\d{0,2}|0)\.){4}", IP + '.') is not None
                and all(0 <= int(p) <= 255 for p in IP.split('.'))):
            return 'IPv4'
        if re.fullmatch(r"(([\dA-Fa-f]{1,4}):){8}", IP + ':'):
            return 'IPv6'
        return 'Neither'

    def validIPAddress(self, IP: str) -> str:
        # return self.rule_match(IP)
        return self.using_regex(IP)
