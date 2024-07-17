# weather-radar-backend
1. 通过Python和NFS实现的雷达预报产品展示系统，前端不需要PgFeature叠加Tiff图层，直接通过nc文件转成png供前端展示
2. 通过SpringBoot、PostgreSQL、Redis及RabbitMQ实现雷达数据的栅格化切片，并进行区划统计及等值面绘制（仅保留了相关部分的微服务模块edc-real-analysis及edc-raster）
