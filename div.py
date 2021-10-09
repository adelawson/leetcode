def div(dividend,divisor):
    if dividend == divisor :
        return 1
    if (divisor < 0 and dividend > 0) or(divisor > 0 and dividend < 0)  :
        divisor = abs(divisor)
        dividend = abs(dividend)
        i = 0
        while dividend > divisor:
            dividend = dividend-divisor
            i+=1
        return -i
    if (divisor<0 and dividend <0):
        divisor = abs(divisor)
        dividend = abs(dividend)
        i = 0
        while dividend > divisor:
            dividend = dividend-divisor
            i+=1
        return i
        
