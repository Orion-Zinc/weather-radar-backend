import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


def nc_to_png(input_file, output_file):
    # 打开NetCDF文件
    ds = xr.open_dataset(input_file)

    # 获取数据变量
    data_var = "ACCRain"  # 将"data_var_name"替换为您实际的数据变量名称

    # 读取数据变量的值
    data = ds[data_var].values

    # 将数值为0的部分设置为透明
    data_transparent = np.where(data == 0, np.nan, data)

    # 创建一个1000x1000的网格
    grid = np.zeros((1000, 1000))

    # 将图像放置在网格的适当位置上
    x_start = 0  # 图像在x轴上的起始位置
    y_start = 0  # 图像在y轴上的起始位置
    x_end = x_start + data_transparent.shape[1]  # 图像在x轴上的结束位置
    y_end = y_start + data_transparent.shape[0]  # 图像在y轴上的结束位置
    grid[y_start:y_end, x_start:x_end] = data_transparent

    # 绘制网格
    plt.imshow(grid, cmap='gray')

    # 绘制PNG图像，并将背景色设置为透明
    # plt.imshow(data_transparent, alpha=1.0, cmap='gray')  # 将alpha值设置为1.0以实现完全不透明的背景色
    # plt.imshow(data_transparent, cmap='rainbow')

    # 可选：设置图像的其他属性，如坐标轴、标题等
    # 隐藏X轴和Y轴的刻度和标签
    plt.axis('off')

    # 设置坐标轴范围
    plt.xlim(0, 999)
    plt.ylim(0, 999)

    # 保存PNG图像
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0, transparent=True)  # 设置transparent=True以保存透明背景的图像

    plt.show()
    plt.close()


if __name__ == "__main__":
    # 调用函数进行转换
    input_file = '20231110_235000.nc'
    output_file = '1213-DBZ.png'
    nc_to_png(input_file, output_file)