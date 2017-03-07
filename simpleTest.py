# -*- coding:utf-8 -*-
"""
Test the wordcloud library.
Generating a  wordcloud image from a text using default argumants.
"""

from os import path
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
from PIL import Image
from pylab import *
import matplotlib.pyplot as plt

#Read the whole text.
#注意因为读入的文本是中文的，所以需要进行中文解码，否则是无法正确读取内容
text = open(u"多情剑客无情剑.txt").read().decode('gbk')
#text = open(u"道士下山.txt").read().decode('utf-8')

#源代码中的默认字体不能显示中文，所以需要将支持中文的字体作为参数传入，这里使用的是微软雅黑。
font = path.join(path.dirname(__file__),'MSYH.TTC')

#mask图像必须是0-255的数据，为了处理任意图像，需要对其进行二值化处理。但是，如果图像的整体灰度值比较接近的话，效果并不是很好，更好的方法是提取图像中的轮廓边缘，然后设置mask。
def convert_to_binary(img):
  img = array(img)
  r = img[:,:,0]
  g = img[:,:,1]
  b = img[:,:,2]
  r = 0.3*r + 0.59*g + 0.11*b
  for i in range(r.shape[0]):
    for j in range(r.shape[1]):
      if int(r[i,j]) > 127:
        r[i,j] = 255;
      else:
        r[i,j] = 0;
  return r

#mask图像可以指定词云的形状
img = Image.open(path.join(path.dirname(__file__),'mask2.jpg'))
#back_coloring = img.convert('L')
back_coloring = convert_to_binary(img)

#显示mask图像
#plt.imshow(back_coloring)
#plt.show()

#生成词云图像
cloudImg = WordCloud(font_path = font,
  background_color="black",   #背景颜色
  max_words=2000,          #词云显示的最大词数
  mask = back_coloring,    #设置词云的形状
  random_state = 42,
  ).generate(text)

plt.imshow(cloudImg)
plt.axis("off")

cloudImg2 = WordCloud(font_path = font,
  background_color="black",   #背景颜色
  max_words=2000,          #词云显示的最大词数
  mask = back_coloring,    #设置词云的形状
  random_state = 42,
  max_font_size = 40
  ).generate(text)
plt.figure()
plt.imshow(cloudImg2)
plt.axis("off")
plt.show()
