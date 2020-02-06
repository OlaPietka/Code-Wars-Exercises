from collections import Counter

def primeFactors(n):
    factor = 2
    factors = []
    
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n /= factor
            factors.append(factor)
    if n > 1:
        factors.append(int(n))
    
    c = Counter(factors)    
    
    out = ["({})".format(i) if c[i] == 1 else "({}**{})".format(i, c[i]) for i in sorted(set(factors))]
    return "".join(out)
            