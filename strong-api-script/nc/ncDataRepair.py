import schedule
import time
import datetime
import psycopg2
import configparser
import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os



# 查询文件是否被添加过
def queryFileExistential(fileName):
    dbConfig = getDatabaseConfig('siyuRadar.ini', 'postgresql')
    connection = psycopg2.connect(**dbConfig)
    cursor = connection.cursor()
    cursor.execute(f"select * from dwh_result.sta_radar_report_png where path = '{fileName}'")
    result = cursor.fetchall()
    # 关闭数据库连接
    cursor.close()
    connection.close()
    return result


def printCurrentTime():
    # 读取配置文件中的nc路径
    pathConfig = getPathConfig('siyuRadar.ini', 'path')
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("当前时间:", currentTime)
    productType = ["ACC005","ACC010","ACC015","ACC030","ACC060","ACC120","RI"]
    # 解析获取当天对应的路径
    currentDate = datetime.date.today()
    currentDateStr = currentDate.strftime("%Y/%m/%d")
    # 临时模拟环境变量
    # ncOrgPath= "/home/radarSoft/workdir"
    ncOrgPath = pathConfig.get("ncpath") + "/QPE" + currentDateStr
    pngTargetPath = pathConfig.get("pngpath") + "/QPE" + currentDateStr
    virtualPath = pathConfig.get("virtualpath") + "/QPE" + currentDateStr
    # 遍历所有产品类型
    for type in productType:
        print(ncOrgPath + "/" + type)
        # 获取路径下所有文件，并与数据库进行比对
        fileNames = [f for f in os.listdir(ncOrgPath) if os.path.isfile(os.path.join(ncOrgPath, f)) and f.endswith('.nc')]
        print(fileNames)
        # 未从Nc处理成png的文件列表
        newNcNames = []
        # 遍历文件列表，查询数据库并处理结果
        for fileName in fileNames:
            result = queryFileExistential(ncOrgPath + "/" + type + "/" +fileName)
            if len(result) == 0:
                newNcNames.append(fileName)
        for fileName in newNcNames:
            # 生成png
            nc_png_file(ncOrgPath + "/" + type + "/" +fileName, pngTargetPath + "/" + type + "/" +fileName)
            # 存储png路径
            addPngRecord(type, virtualPath + "/" + type + "/" +fileName, fileTimeDetector(fileName))


#读取数据库配置
def getDatabaseConfig(filename, section):
    config = configparser.ConfigParser()
    config.read(filename)
    dbConfig = {}
    if config.has_section(section):
        params = config.items(section)
        for param in params:
            dbConfig[param[0]] = param[1]
    else:
        raise Exception(f"Section '{section}' not found in the {filename} file")
    return dbConfig

# 读取文件存储路径
def getPathConfig(filename, section):
    config = configparser.ConfigParser()
    config.read(filename)
    pathConfig = {}
    if config.has_section(section):
        params = config.items(section)
        for param in params:
            pathConfig[param[0]] = param[1]
    else:
        raise Exception(f"Section '{section}' not found in the {filename} file")
    return pathConfig

# 为新生成的图片增加一条记录
def addPngRecord(type, path, time):
    dbConfig = getDatabaseConfig('siyuRadar.ini', 'postgresql')
    conn = psycopg2.connect(**dbConfig)
    cursor = conn.cursor()
    insertQuery = "insert into dwh_result.sta_radar_report_png (type,path,time) values(%s,%s,%s)"
    data = (type, path, time)
    cursor.execute(insertQuery, data)
    conn.commit()
    cursor.close()
    conn.close()

# 将nc处理成png并输出
def nc_png_file(input_file, output_dir):
    nc_obj = nc.Dataset(input_file)
    # pre = np.array(nc_obj.variables['ACCRain'])
    pre = np.array(nc_obj.variables['RI'])
    Lon = np.array(nc_obj.variables['Longitude'])
    Lat = np.array(nc_obj.variables['Latitude'])
    nc_obj.close()
    colors = [(0, '#9dee84'),  # 灰色#a4a4a4
              (0.7, '#a4a4a4'),  # 浅绿色#9dee84
              (0.8, '#0000fd'),
              (0.9, '#f804f8'),
              (1, '#740438')]
    xlims = [115.4155, 119.93973]
    ylims = [33.8243, 37.43738]
    plt.xlim(xlims)
    plt.ylim(ylims)
    fig = plt.figure(figsize=(12, 9))
    pre[pre <= 0] = np.nan
    levels = np.linspace(-5, 80, 16)
    # plt.contourf(Lon, Lat, pre, cmap='rainbow', levels=levels, extend='both')
    plt.contourf(Lon, Lat, pre, cmap=LinearSegmentedColormap.from_list('custom_cmap', colors), levels=levels, extend='both')
    plt.colorbar().remove()  # 移除图例
    plt.grid()
    plt.axis('off')
    input_file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, input_file_name + ".png")
    plt.savefig(output_file, transparent=True, dpi=300)
    plt.close()

# 解析文件名对应的时间
def fileTimeDetector(fileName):
    # 提取日期和时间信息
    dateStr, timeStr = fileName.split('_')
    timestamp_obj = datetime.datetime.combine(datetime.datetime.strptime(dateStr, "%Y%m%d"), datetime.datetime.strptime(timeStr, "%H%M%S"))
    return timestamp_obj.timestamp()

# 单次执行
printCurrentTime()
# addPngRecord()
# 指定文件路径
# path = 'D:\\WorldView\\DaWenHe\\radar\\demo\\radarSource\\QPE\\2023\\11\\10\\ACC005'
# # 获取文件路径下的所有文件名
# fileNames = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.nc')]
# print(fileNames)


# 定时执行
# schedule.every(1).minutes.do(print_current_time)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

