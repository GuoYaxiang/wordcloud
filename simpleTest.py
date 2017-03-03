# -*- coding:utf-8 -*-
"""
Test the wordcloud library.
Generating a  wordcloud image from a text using default argumants.
"""

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Read the whole text.
#注意因为读入的文本是中文的，所以需要进行中文解码，否则是无法正确读取内容
text = open(u"多情剑客无情剑.txt").read().decode('gbk')
#text = open(u"道士下山.txt").read().decode('utf-8')

#源代码中的默认字体不能显示中文，所以需要将支持中文的字体作为参数传入，这里使用的是微软雅黑。
font = path.join(path.dirname(__file__),'MSYH.TTC')


#生成词云图像
cloudImg = WordCloud(font_path = font).generate(text)

plt.imshow(cloudImg)
plt.axis("off")

cloudImg2 = WordCloud(font_path = font, max_font_size = 40).generate(text)
plt.figure()
plt.imshow(cloudImg2)
plt.axis("off")
plt.show()
