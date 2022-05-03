from util import *
class Decryptor:
    def decrypt(self,C,d,n):
        return quick_exp_mod(C,d,n)