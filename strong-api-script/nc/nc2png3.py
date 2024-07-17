import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def nc_png_file(input_file, output_dir):
    nc_obj = nc.Dataset(input_file)
    pre = np.array(nc_obj.variables['ACCRain'])
    Lon = np.array(nc_obj.variables['Longitude'])
    Lat = np.array(nc_obj.variables['Latitude'])
    nc_obj.close()

    xlims = [115.4155, 119.93973]
    ylims = [33.8243, 37.43738]

    colors = [(0, '#9dee84'),  # 灰色#a4a4a4
              (0.7, '#a4a4a4'),  # 浅绿色#9dee84
              (0.8, '#0000fd'),
              (0.9, '#f804f8'),
              (1, '#740438')]

    plt.xlim(xlims)
    plt.ylim(ylims)

    fig = plt.figure(figsize=(12, 9))
    pre[pre <= 0] = np.nan
    # levels = np.linspace(-5, 80, 16)
    levels = np.linspace(0, 251, 100)
    plt.contourf(Lon, Lat, pre, cmap=LinearSegmentedColormap.from_list('custom_cmap', colors), levels=levels, extend='both')
    plt.colorbar().remove()  # 移除图例
    plt.grid()
    plt.axis('off')
    plt.savefig("test" + ".png", transparent=True, dpi=300)
    plt.show()
    plt.close()

# 输入文件路径
input_file = "20231110_235000.nc"
# 输出文件夹路径
output_dir = "output3.png"

nc_png_file(input_file, output_dir)
