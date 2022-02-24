"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time


class BinaryNumber:
    """ done """

    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return 'decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec))

    def __add__(self, other):
        return BinaryNumber(self.decimal_val + other.decimal_val)

    def __mul__(self, other):
        return BinaryNumber(self.decimal_val * other.decimal_val)

    def __sub__(self, other):
        return BinaryNumber(self.decimal_val - other.decimal_val)


# Implement multiplication functions here. Note that you will have to
# ensure that x, y are appropriately sized binary vectors for a
# divide and conquer approach.

def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
    return (binary2int(vec[:len(vec) // 2]),
            binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


def quadratic_multiply(x, y):
    return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):

    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return x * y

    x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)

    n = len(x.binary_vec)
    print("n: %s" % n)

    xl, xr = split_number(x.binary_vec)

    yl, yr = split_number(y.binary_vec)

    print("X: %s" % x.binary_vec)
    print("Y: %s" % y.binary_vec)
    print("XL: %s" % xl.binary_vec)
    print("XR: %s" % xr.binary_vec)
    print("YL: %s" % yl.binary_vec)
    print("YR: %s" % yr.binary_vec)
    ll = _quadratic_multiply(xl, yl)
    rr = _quadratic_multiply(xr, yr)

    lrrl = _quadratic_multiply(xl * xr + yl * yr)

    bs1 = bit_shift(BinaryNumber(2), n)
    bs2 = bit_shift(BinaryNumber(2), n // 2)

    total = bs1*ll + bs2* lrrl * rr

    return total

    # 2 and 2 as inputs
    # xl = 1 xr = 0, yl = 1 yr = 0
    # ll = 1, rr = 0, lrrl = 1+0 * 1+0 = 1
    # n = 2
    # 2^1 * 1 = 4
    # 2^1 * 1 = 2
    # rr = 0
    # 4 + 2 + 0 = 6


# Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start) * 1000


if __name__ == "__main__":
    x = BinaryNumber(2)
    y = BinaryNumber(3)
    print(_quadratic_multiply(x, y))
