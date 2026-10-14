class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits manually
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit

            # 4. Handle 32-bit overflow
            if sign * num > INT_MAX:
                return INT_MAX
            if sign * num < INT_MIN:
                return INT_MIN

            i += 1

        return sign * num
