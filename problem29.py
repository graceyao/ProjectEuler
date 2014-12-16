import math

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factors(num):
    facts = []
    for i in range(2, num + 1):
        if is_prime(i):
            if num % i == 0:
                facts.append(i)
    return facts

def factorization(base):
    primes = [] # tuples of (base, exponent)
    fs = factors(base)
    for factor in fs:
        times = 0
        num = base
        while num % factor == 0:
            num /= factor
            times += 1
        primes.append((factor, times))
    return primes

def exponents(base, exponent):
    bases = factorization(base)
    new_bases = []

    for b, e in bases:
        e *= exponent
        new_bases.append((b, e))

    return new_bases

def real_deal():
    lst = []
    for a in range(2, 101):
        for b in range(2, 101):
            e = exponents(a, b)
            if e not in lst:
                lst.append(e)
    return lst

print len(real_deal())