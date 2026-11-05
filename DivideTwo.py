class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) ^ (divisor < 0)
        dividend_abs, divisor_abs = abs(dividend), abs(divisor)
        quotient = 0
        
        while dividend_abs >= divisor_abs:
            temp_divisor, multiple = divisor_abs, 1
            while dividend_abs >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend_abs -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient
