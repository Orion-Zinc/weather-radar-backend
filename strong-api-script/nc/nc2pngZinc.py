import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # 打开nc文件
    file_path = 'D:\\WorldView\\DaWenHe\\radar\\demo\\nc2pngtest\\20231110_235000.nc'
    data = nc.Dataset(file_path)

    # 获取变量数据
    var_name = 'your_variable'
    variable = data[var_name]

    # 获取坐标轴的数据
    latitude = data['latitude']
    longitude = data['longitude']

    # 创建网格
    lon, lat = np.meshgrid(longitude[:], latitude[:])

    # 绘制地图
    plt.figure(figsize=(10, 8))
    plt.contourf(lon, lat, variable[:])
    plt.colorbar()

    # 设置标题和坐标轴标签
    plt.title('Your Plot Title')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # 保存为png文件
    output_path = 'D:\\WorldView\\DaWenHe\\radar\\demo\\nc2pngtest\\output.png'
    plt.savefig(output_path)

    # 关闭nc文件
    data.close()

