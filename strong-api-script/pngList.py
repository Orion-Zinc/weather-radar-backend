import requests
import time
import hashlib
import json

def print_hi(name):
    print(f" {name}")
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

# 发送GET请求
response = requests.get("http://10.37.3.130:10001/radar/v1/thrid/images/realtime?category=DSD_DMP&beginTime=2023-11-10%2008:00:00&endTime=2023-11-11%2023:00:00",
                        headers=headers,
                        json=data)
# 获取响应的字节数据并进行解码
response_text = response.content.decode('utf-8')
# 将字符串对象转换为JSON对象
response_json = json.loads(response_text)
formatted_json = json.dumps(response_json, indent=4, ensure_ascii=False)

print(formatted_json)


if __name__ == '__main__':
    print_hi('')
