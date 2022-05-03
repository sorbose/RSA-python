from util import *
class Encryptor:
    def encrypt(self,M,e,n):
        return quick_exp_mod(M,e,n)
