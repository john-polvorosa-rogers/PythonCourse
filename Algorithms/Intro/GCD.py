# Euclid's Algorithm to find the Greatest Common Denominator
# Two numbers, one greater than the other (a > b)
# Divide a/b, if remainder 0, GCD is b
# else a = b, remainder = b, then repeat until remainder = 0


def gcd(a, b):
    while(b != 0):
        temp = a
        a = b
        b = temp % b
        
        return a

# Output Tests
print (gcd(102,5))
print (gcd(84,4))

# This is wrong!!! SAMPLE FROM LINKEDIN COURSE
# Fixed it with GCD2.py