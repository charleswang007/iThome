#encoding=utf-8
import jieba
import jieba.analyse
from cutecharts.charts import Bar
from cutecharts.charts import Pie


content = open('rose-line.txt', 'rb').read()
words = jieba.lcut(content) # 使用jieba這個library對文檔內容進行分詞
counts = {} # 此為由文字內容對應到出現次數的dictionary

# 進行統計
for word in words:
    if len(word) <= 1: # 排除單個字
        continue
    elif word.isdigit(): # 排除數字
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

# 刪除不重要的詞語
text=' '.join(words)
excludes = {'\r\n','下午','上午','...'} # LINE紀錄會有很多換行，如不去掉分析完會顯示
for exword in excludes:
    try:
        del(counts[exword])
    except:
        continue
    
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True) # 根據單詞出現次數進行排序

# 將出現次數最多的幾個詞畫成圖表
top_words = []
top_counts = []
i = -1
while len(top_words) <= 10:
    i += 1
    word, count = items[i]
    if word == "通話" or word == "照片" or word == "影片" or word == "貼圖" or word == "你的名字" or word == "對方名字":
        continue
    top_words.append(word)
    top_counts.append(count)
chart = Bar("關鍵字圖表")
chart.set_options(labels = top_words, x_label="單詞", y_label="出現次數")
chart.add_series("次數", top_counts)

chart2 = Pie("通話/影片/照片數統計")
chart2.set_options(labels=['照片', '影片', '通話'])
chart2.add_series([counts.get("照片", 0), counts.get("影片", 0), counts.get("通話", 0)])

chart3 = Pie("傳送訊息量")
chart3.set_options(labels=['你的名字', '對方'],inner_radius=0)
chart3.add_series([counts.get("你的名字", 0), counts.get("對方名字", 0)])

chart.render(dest="關鍵字.html")
chart2.render(dest="通話/影片/照片數統計.html")
chart3.render(dest="傳送訊息量.html")