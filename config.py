#coding = 'utf-8'

'''
配置文件
'''

# style规则参考./README.md
# 正常地图样式，保留地图背景，确保街道清晰可见
MY_STYLE = [
{
"featureType": "road",
"elementType": "all",
"stylers": {
"visibility": "on",
"color": "#7a7a7aff",  # 灰色道路，清晰但不过于突兀
"weight": 1.5  # 适当加粗道路
}
},
{
"featureType": "highway",
"elementType": "all",
"stylers": {
"color": "#ff9900ff",  # 高亮显示高速公路
"weight": 2  # 高速公路加粗
}
},
{
"featureType": "arterial",
"elementType": "all",
"stylers": {
"color": "#0066ccff",  # 主路用蓝色突出
"weight": 1.8  # 主路适当加粗
}
},
{
"featureType": "land",
"elementType": "all",
"stylers": {
"color": "#f2f2f2ff"  # 浅灰色陆地背景
}
},
{
"featureType": "water",
"elementType": "all",
"stylers": {
"color": "#a9d1f5ff"  # 浅蓝色水体
}
},
{
"featureType": "green",
"elementType": "all",
"stylers": {
"color": "#99cc99ff"  # 绿色表示绿地
}
},
{
"featureType": "building",
"elementType": "all",
"stylers": {
"color": "#ccccccff",  # 灰色建筑
"visibility": "on"
}
},
{
"featureType": "poilabel",
"elementType": "labels.text",
"stylers": {
"visibility": "on",  # 保留兴趣点标签
"fontsize": 10
}
}
]

# 行政区名
TARGET_NAME = "北京市"

# 行政区号（北京市）
TARGET_CODE = 110000

# 根目录
ROOT_DIR = './res'

# 4-18，不同要素显示等级不同，参考README.md
# 设置为12级（适合查看城市街道）
TARGET_LEVEL = 12

# 是否保留瓦片
SAVE_TILE = True

# 是否合成瓦片为一张地图（False表示只下载瓦片不合成）
MERGE_TO_MAP = True

# 爬遥感影像时level是否由系统决定
AUTO_LEVEL = False

# 目标突出要素
TARGET_OBJECT = "正常地图"

# 个性地图0；遥感影像1
TARGET_TYPE = 0

# 图片保存格式，默认png，支持jpg等
IMAGE_FORMAT = 'png'

# 是否绘制边界
B_ISDRAW = True

# 边界的样式
B_STYLE = {
	'color': (0,0,255),# BGR顺序，即(blue, green, red)，颜色值0-255
	'thick': 3 #线宽
}

# 矩形范围还是行政区,0：矩形，1：行政区
RECT_OR_DISTRICT = 1

# 矩形范围,西南和东北角经纬度WGS84坐标（当RECT_OR_DISTRICT=1时此项无效）
RECT_BOX = \
[(115.7,28.6),(116.1,28.8)]