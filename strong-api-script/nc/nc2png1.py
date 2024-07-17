import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
import os

def nc_png_file(input_file, output_dir):
    nc_obj = nc.Dataset(input_file)
    pre = np.array(nc_obj.variables['ACCRain'])
    Lon = np.array(nc_obj.variables['Longitude'])
    Lat = np.array(nc_obj.variables['Latitude'])
    nc_obj.close()

    xlims = [115.4155, 119.93973]
    ylims = [33.8243, 37.43738]

    plt.xlim(xlims)
    plt.ylim(ylims)

    fig = plt.figure(figsize=(12, 9))
    pre[pre <= 0] = np.nan
    # 将数值为0的部分设置为透明
    pre = np.where(pre == 0, np.nan, pre)
    plt.imshow(pre, alpha=1.0, cmap='gray')  # 将alpha值设置为1.0以实现完全不透明的背景色
    levels = np.linspace(-5, 80, 16)
    # plt.contourf(Lon, Lat, pre, cmap='rainbow', levels=levels, extend='both')
    plt.contourf(Lon, Lat, pre, cmap='rainbow', levels=levels, extend='both')
    plt.colorbar()
    plt.grid()
    plt.axis('off')
    plt.savefig(output_dir)
    plt.show()
    plt.close()

# 输入文件夹路径
input_dir = "D:\\WorldView\\DaWenHe\\radar\\demo\\radarSource\\QPE\\2023\\11\\10\\ACC120"
# 输出文件夹路径
output_dir = "D:\\WorldView\\DaWenHe\\radar\\demo\\radarSource\\QPE\\2023\\11\\10\\ACC120\\output"

# 遍历输入文件夹下的所有文件
for file_name in os.listdir(input_dir):
    # Generating the full path of each input file
    input_file = os.path.join(input_dir, file_name)

    if os.path.isfile(input_file) and not file_name.startswith('.') and file_name.endswith('.nc'):
        nc_png_file(input_file, output_dir)