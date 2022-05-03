import math
from random import randint

class PrimeGenerator:
    def __miller_rabin(self, p):
        if p == 1: return False
        if p == 2: return True
        if p % 2 == 0: return False
        m, k, = p - 1, 0
        while m % 2 == 0:
            m, k = m // 2, k + 1
        a = randint(2, p - 1)
        x = pow(a, m, p)
        if x == 1 or x == p - 1: return True
        while k > 1:
            x = pow(x, 2, p)
            if x == 1:
                return False
            if x == p - 1:
                return True
            k = k - 1
        return False

    def is_prime(self, p, r=32):
        for i in range(r):
            if self.__miller_rabin(p) == False:
                return False
        return True

    def gen_rand_prime(self, lower, upper):
        x = randint(lower, upper)
        if x % 2 == 0:
            x += 1
        while self.is_prime(x) == False:
            x += 2
        return x


class KeyGenerator:
    def get_key(self):
        primeGenerator = PrimeGenerator()
        # 生成大素数p,q，p,q的值尽量避免过于接近
        p = primeGenerator.gen_rand_prime(2 ** 800, 2 ** 900)
        q = primeGenerator.gen_rand_prime(2 ** 1248, 2 ** 1298)
        print(f"p:{p}\nq:{q}")
        # n的位数至少是2048位
        n = p * q
        # 计算φ(n)
        phi = (p - 1) * (q - 1)
        # e不需要选太大
        e = randint(3, 2**128)
        while math.gcd(e, phi) != 1:
            e = randint(3, 2**128)
        # 求解ax+by=1时,e对应a，φ(n)对应b,d对应x，k对应-y
        _, x, y = self.__exgcd(e, phi)
        # 确保d>0
        if x<=0:
            x+=phi
            y-=e
        d = x
        k = -y
        # 验证结果是否是1
        print(e*d-k*phi)
        return n, e, d, k,phi

    def __exgcd(self, a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y
