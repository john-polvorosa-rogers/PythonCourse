# Euclid's Algorithm to find the Greatest Common Denominator
# Two numbers, one greater than the other (a > b)
# Divide a/b, if remainder 0, GCD is b
# else a = b, remainder = b, then repeat until remainder = 0

def gcd2(a, b):
    while(b != 0):
        r = a % b
        if (r == 0):
            return b
        else:
            while(r!=0):
                temp = a
                a = b
                b = r
                r = temp % b
            return b