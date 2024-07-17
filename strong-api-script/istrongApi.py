# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import hashlib

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 密钥key和密钥Secret
key = "NXDff9TcCT5W0kwa8xhmtNxRj62xzhwb"
secret = "YwGFZwzAwa1nyzpFJTRY9J49tjsHyJNZ"

# 获取当前时间戳（精确到秒）
timestamp = str(int(time.time()))

# 计算istrongApiSecret
data = key + "_" + secret + "_" + timestamp
md5 = hashlib.md5()
md5.update(data.encode("utf-8"))
istrongApiSecret = md5.hexdigest()

# 输出结果
print("istrongApiKey NXDff9TcCT5W0kwa8xhmtNxRj62xzhwb")
print("istrongApiTimestamp " + timestamp)
print("istrongApiSecret " + istrongApiSecret)