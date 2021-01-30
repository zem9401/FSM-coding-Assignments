class Solution:
    """
    1、读入字符串并丢弃无用的前导空格
    2、检查第一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结
果是负数还是正数。 如果两者都不存在，则假定结果为正。
    3、读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    4、将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没
    5、有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    6、如果整数数超过 32 位有符号整数范围 [−2^31, 2^31− 1] ，需要截断这个整数，
    使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31− 1 的整数应该被固定为 2^31− 1 。
    7、返回整数作为最终结果。
    注意：
    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
    """
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if s == "":
            return 0
        else:
            if s[0] not in ["+", "-"]:
                num = "+"
                s = s
            else:
                num = s[0]
                s = s[1:]
            for i in s:
                if i.isdigit():
                    num += i
                else:
                    break
            if len(num) > 1:
                num = num
            else:
                num = 0
        if int(num) > 2**31-1:
            num = 2**31-1
        elif int(num) < -2**31:
            num = -2**31
        # return max(min(int(num), 2 ** 31 - 1), -2 ** 31)
        return int(num)

if __name__ == '__main__':
    s = Solution()
    num = s.myAtoi("42")
    print(num)
    assert num == 42, "False"
    num = s.myAtoi("   -42")
    print(num)
    assert num == -42, "False"
    num = s.myAtoi("4193 with words")
    print(num)

    assert num == 4193, "False"
    num = s.myAtoi("words and 987")
    print(num)

    assert num == 0, "False"
    num = s.myAtoi("-91283472332")
    print(num)

    assert num == -2 ** 31, "False"
    num = s.myAtoi("21474836460")
    print(num)