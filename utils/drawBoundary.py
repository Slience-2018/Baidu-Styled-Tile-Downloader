# coding='utf-8'

import cv2
import numpy as np
import os

# 绘制行政边界
def drawPoly(picPath, pts, style):
	img = cv2.imdecode(np.fromfile(picPath,dtype=np.uint8),-1)
	isClosed = True
	color = style['color']
	thickness = style['thick']
	for poly in pts:
		p = np.array(poly, np.int32) 
		p = p.reshape((-1, 1, 2)) 
		img = cv2.polylines(img, [p], isClosed, color, thickness)
	# 根据文件扩展名确定编码格式
	extension = os.path.splitext(picPath)[1].lower()
	cv2.imencode(extension, img)[1].tofile(picPath)
