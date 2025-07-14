import decimal


def chudnovsky_pi(n_terms):
    decimal.getcontext().prec = 1000
    C = 426880 * decimal.Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = decimal.Decimal(L)
    for i in range(1, n_terms):
        M = (K ** 3 - 16 * K) * M // i ** 3
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12
    pi = C / S
    return pi


n_terms = 10
result = chudnovsky_pi(n_terms)
print(result)
    