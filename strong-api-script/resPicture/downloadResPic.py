import urllib.request
import requests
import os


# 定义路径和替换值列表
path = 'http://124.205.245.115:19537/pictures/reservoir/雪野水库大坝.jpg'
replace_values = ['金斗水库大坝', '雪野水库大坝', '乔店水库大坝', '大冶水库大坝', '公庄水库大坝', '鹁鸽楼水库大坝', '沟里水库大坝', '葫芦山水库大坝', '杨家横水库大坝', '光明水库大坝', '大河水库大坝', '黄前水库大坝', '胜利水库大坝', '彩山水库大坝', '角峪水库大坝', '山阳水库大坝', '小安门水库大坝', '东周水库大坝', '苇池水库大坝', '田村水库大坝', '尚庄炉水库大坝', '贤村水库大坝', '直界水库大坝', '金水河水库大坝']

# 将替换值逐个替换并下载图片
for value in replace_values:
    replaced_path = path.replace('雪野水库大坝', value)  # 执行替换操作
    filename = replaced_path.split('/')[-1]  # 获取图片文件名

    try:
        response = requests.get(replaced_path)
        response.raise_for_status()  # 检查是否发生网络错误

        with open('D:\\WorldView\\DaWenHe\\sql\\res-pic\\'+ filename, "wb") as file:
            file.write(response.content)

        print(f"Downloaded image: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {filename}: {e}")


