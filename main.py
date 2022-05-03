# https://www.zhihu.com/question/25038691
# 这是一个示例 Python 脚本。
from generator import *
from encryptor import *
from decryptor import *
import sys
import time


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    txt = sys.argv[1]
    T=time.perf_counter()
    M = int.from_bytes(txt.encode('utf-8'), sys.byteorder)
    keyGenerator = KeyGenerator()
    n, e, d, k, phi = keyGenerator.get_key()
    # e=1213;n=9991;d=4117;k=510;phi=9792
    print(f"n: {n}\ne: {e}\nd: {d}\nk: {k}")
    encryptor = Encryptor()
    C = encryptor.encrypt(M, e, n)
    print(f"M:{M}\nC:{C}")
    decryptor = Decryptor()
    M = decryptor.decrypt(C, d, n)
    M = M.to_bytes(1024, sys.byteorder).decode('utf8').rstrip('\x00')
    print(M)
    print(f"Time: {time.perf_counter()-T}")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
