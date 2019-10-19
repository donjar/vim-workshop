import os
import sys
import math
import fractions
import hashlib

if __name__ == '__main__':
    print(os.getenv('PATH'))
    print(sys.argv)
    print(math.pi)
    print(fractions.Fraction('0.7'))
    print(hashlib.sha1(b'vim').hexdigest())
