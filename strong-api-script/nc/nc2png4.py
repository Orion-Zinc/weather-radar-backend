import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os

def nc_png_file(input_file, output_dir):
    nc_obj = nc.Dataset(input_file)
    pre = np.array(nc_obj.variables['ACCRain'])
    # pre = np.array(nc_obj.variables['RI'])
    Lon = np.array(nc_obj.variables['Longitude'])
    Lat = np.array(nc_obj.variables['Latitude'])
    nc_obj.close()

    colors = [(0, '#9dee84'),  # 灰色#a4a4a4
              (0.7, '#a4a4a4'),  # 浅绿色#9dee84
              (0.8, '#0000fd'),
              (0.9, '#f804f8'),
              (1, '#740438')]
    # 115.54215 120.066185
    #  33.82097  37.434048
    # xlims = [115.542, 120.066]
    # ylims = [33.82097, 37.434048]
    xlims = [115.358, 119.894]
    ylims = [33.912, 37.528]

    plt.xlim(xlims)
    plt.ylim(ylims)

    # fig = plt.figure(figsize=(12, 9))
    fig = plt.figure(figsize=(10/3, 10/3), dpi=1)
    pre[pre <= 0] = np.nan
    # levels = np.linspace(-5, 80, 100)
    # # plt.contourf(Lon, Lat, pre, cmap='rainbow', levels=levels, extend='both')
    # plt.contourf(Lon, Lat, pre, cmap=LinearSegmentedColormap.from_list('custom_cmap', colors), levels=levels, extend='both')
    # 演示汇报用
    levels = np.linspace(0, 0.12, 12)
    plt.contourf(Lon, Lat, pre, cmap=LinearSegmentedColormap.from_list('custom_cmap', colors), levels=levels, extend='both')
    plt.colorbar().remove()  # 移除图例
    plt.grid()
    plt.axis('off')

    # Extracting the input file name without extension
    input_file_name = os.path.splitext(os.path.basename(input_file))[0]

    # Generating the corresponding PNG file name
    output_file = os.path.join(output_dir, input_file_name + ".png")

    plt.savefig(output_file, transparent=True, dpi=300)
    plt.close()

# 输入文件夹路径
input_dir = "D:\\WorldView\\DaWenHe\\radar\\demo\\radarSource2\\QPE\\2023\\11\\11\\ACC060"
# 输出文件夹路径
output_dir = "D:\\WorldView\\DaWenHe\\radar\\demo\\radarSource2\\QPE\\2023\\11\\11\\ACC060\\output2"

# 遍历输入文件夹下的所有文件
for file_name in os.listdir(input_dir):
    # Generating the full path of each input file
    input_file = os.path.join(input_dir, file_name)

    if os.path.isfile(input_file) and not file_name.startswith('.') and file_name.endswith('.nc'):
        nc_png_file(input_file, output_dir)