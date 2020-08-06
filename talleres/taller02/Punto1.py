#p>q
def gcd_euclid(p, q):
    if q==0:
        return p
    else:
        return gcd_euclid(q, p % q)

print(gcd_euclid(100, 3))
