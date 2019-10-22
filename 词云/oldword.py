import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

df = pd.read_excel(r'1.xlsx', sheet_name='Q32',) # ['Q29','Q30','Q31', 'Q32']
font = r"C:\WINDOWS\Fonts\simhei.ttf"
lis = []
eliminate = ['无', ',', '，', '6', '!', '1', '。', '！']
for data in df['答案'].values:
    if "受访人数" in data:
        break

    if data not in eliminate:
        for i in jieba.lcut(data):
            lis.append(i)

    # for i in jieba.lcut(data):
    #     lis.append(i)

str_list = ','.join(lis)
w = WordCloud(scale=24, font_path=font, background_color="white")
w.generate(str_list)
# plt.imshow(w, interpolation="bilinear")
# plt.axis("off")
# plt.show()
w.to_file('研究生对学校、研究生院、培养学院的总体评价(不过滤).png')

