# 为yolo训练进行数据增强
## 运行环境
> python3.7
> imgaug
> opencv
imaug库在[这里下载](https://github.com/aleju/imgaug)

imaug使用[参考文档](https://khan.github.io/KaTeX/)



## 使用方法
 main.py是主文件
	参数设定
	>`image_load_path` = path:只含传入图像的文件夹
	>`text_load_path` =path: 只含传入参TXT的文件夹。
	>`image_result_path` =path: 处理后图像存储的文件夹
	>`text_result_path` =path: 处理后TXT存储的文件夹
	>`num`=生成图像的数量
