import requests
import time
import hashlib
import json
from PIL import Image
from io import BytesIO

def print_hi(name):
    print(f"Hi, {name}")


"""
雷达nc列表接口（用于获取）
"""
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

# 设置请求头
headers = {
    "istrongApiKey": "NXDff9TcCT5W0kwa8xhmtNxRj62xzhwb",
    "istrongApiTimestamp": timestamp,
    "istrongApiSecret": istrongApiSecret
}

# 设置请求体
data = {
    "type": "QPE_ACC060",
    # "forecastTime": "2023-11-10 23:40:00",
    "dilution": 1,
    "time": "2023-11-10 22:00:00",
}
# data = {
#     "type": "QPE_ACC005",
#     "dilution": 4,
#     "time": "2023-11-11 02:35:00"
# }
# data = {"time":"2023-11-10 22:00:00","type":"QPF_ACC005","forecastTime":"2023-11-10 23:00:00}","dilution":1}


# 发送POST请求
response = requests.post("http://10.37.3.130:10001/radar/v1/thrid/nc/tiff", headers=headers, json=data)
#指定要保存的文件名和路径
file_path = "D:\\WorldView\\DaWenHe\\radar\\new-response-png\\0110tiff"

with open(file_path, "wb") as f:
    f.write(response.content)


if __name__ == '__main__':
    print_hi('')
