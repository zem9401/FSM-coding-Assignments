class Solution:
    """
    有效数字（按顺序）可以分成以下几个部分：
    一个 小数 或者 整数
    （可选）一个 'e' 或 'E' ，后面跟着一个 整数
    小数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    下述格式之一：
    至少一位数字，后面跟着一个点 '.'
    至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    一个点 '.' ，后面跟着至少一位数字
    整数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    至少一位数字
    部分有效数字列举如下：
    ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    部分无效数字列举如下：
    ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
    """
    def isNumber(self, s: str) -> bool:
        try:
            if s[0].lower() == "e":
                return False
            elif s == "." or s == "0e":
                return False
            if float(s) or float(s) == 0:
                return True
            else:
                return False
        except:
            return False

if __name__ == '__main__':
    s = Solution()
    num = s.isNumber("0")
    print(num)
    num = s.isNumber("e")
    print(num)