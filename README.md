# SARS-CoV 感染率检测
- 从丁香园爬取数据，基于所有省份数据 (31省份，按照身份人口归一化)，计算平均每万人每天感染新型冠状病毒人数数据。

- source url: "https://3g.dxy.cn/newh5/view/pneumonia_timeline?whichFrom=peopleapp"

- 结果展示 

# 环境、语言、模块
  - 需要使用 selenium 模拟打开 浏览器，如 Chrome 浏览器 
  - 基于 python3 使用 selenium 和 bs4 模块
  
# 数据说明
  - city_name_all  全国所有省会以及城市名称
  - pro_name  全国所有省会名称
  - pro2city  省会城市与城市对应字典，如 {'湖南':['长沙','永州',]}。pickle 序列化数据
  - pro2num   全国各省与人口对应字典，如 {'湖北': 5800}。pickle 序列化数据
  
# 运行
  - python 1get_data.py 。 从目标网址 获取 疫情动态，得到 data_raw_当日日期，如data_raw_2020-01-28。
  - python 2process_raw_data.py。 得到 data_raw_当日日期_rd，如data_raw_2020-01-28_rd。得到每个城市每日新增的病例情况。```对于报错，需要手动修改data_raw_2020-01-28数据，满足  xxx新增xx例 即可```
  - python main.py 得到 all_日期.png 和 no_hubei日期.png 两个图像，分别是全国所有城市的平均情况，湖北省单独的情况，全国去除湖北省以外的其他城市平均情况。```main.py 文件中，line 51 日期列表需要手动配置,如[118,119,120,121,122,123]。 line 87 时间跨度，需要手动配置。具体见代码```

                   
