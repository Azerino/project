import numpy as np
from sympy.ntheory import isprime, primefactors

def generatorp(p):
    """Return a generator for the cyclic group multiplication modulo p.
    Also called a primitive root of p.

    Args:
        p (int): a prime number

    Raises:
        RuntimeError: when p is not a prime

    Returns:
        int: the generator
    """
    if not isprime(p):
        raise RuntimeError(str(p) + " is not prime")

    primef = np.array(primefactors(p-1), dtype="int")
    g = 2
    i = 1
    while i <= np.size(primef):
        if 1 == pow(int(g), int((p-1)/primef[i-1]), int(p)):
            g = g + 1
            i = 0
        i = i + 1
    return g