import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.features import DivIcon
from branca.element import Template, MacroElement
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime
# https://nbviewer.org/gist/talbertc-usgs/18f8901fc98f109f2b71156cf3ac81cd

with open("/Users/seokcheon/Library/CloudStorage/OneDrive-Personal/CIT/Technovation-Girls/rok---report-of-kickboard-default-rtdb-export.json", "r") as f:
	data = json.load(f)

months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
months_n = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
total = 0

# 지쿠터, 스윙, 빔, 씽씽
brands = [0, 0, 0, 0]
labels = ['GCOOTER', 'SWING', 'BEAM', 'SINGSING']
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', \
        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

latitudes = []
longitudes = []
brand_name = []

today = datetime.datetime.now()
month = ""
year = str(today.year)

if(today.month < 10):
    month = '0'+str(today.month)
else:
    month = str(today.month)

# choice = input('Enter the month to get statistics.(01 ~ 12)\nMonth : ')
choice = month
choice_month = [0, 0, 0, 0]

# 브랜드 별 횟수, 순서는 지쿠터, 스윙, 빔, 씽씽
# 월 별 횟수
cnt = 0
for k in months_n:
    for i in days:
        try:
            day = list(data["User-data"][year][k][i])
            # print(day)
            for j in day:
                if(data["User-data"][year][k][i][j]["kickboard"] == '"GCOOTER"'):
                    brands[0] += 1
                    brand_name.append("GCOOTER")
                    months[cnt] += 1
                elif(data["User-data"][year][k][i][j]["kickboard"] == '"SWING"'):
                    brands[1] += 1
                    brand_name.append("SWING")
                    months[cnt] += 1
                elif(data["User-data"][year][k][i][j]["kickboard"] == '"BEAM"'):
                    brands[2] += 1
                    brand_name.append("BEAM")
                    months[cnt] += 1
                elif(data["User-data"][year][k][i][j]["kickboard"] == '"SINGSING"'):
                    brands[3] += 1
                    brand_name.append("SINGSING")
                    months[cnt] += 1

                latitudes.append(data["User-data"][year][k][i][j]["latitude"])
                longitudes.append(data["User-data"][year][k][i][j]["longitude"])
                
        except:
            continue
    cnt += 1

# print(brands)
# print(months)

# 월 통계
cnt = 0
for k in months_n:
    for i in days:
        try:
            day = list(data["User-data"][year][k][i])
            # print(day)
            for j in day:
                if(data["User-data"][year][choice][i][j]["kickboard"] == '"GCOOTER"'):
                    choice_month[0] += 1
                elif(data["User-data"][year][choice][i][j]["kickboard"] == '"SWING"'):
                    choice_month[1] += 1
                elif(data["User-data"][year][choice][i][j]["kickboard"] == '"BEAM"'):
                    choice_month[2] += 1
                elif(data["User-data"][year][choice][i][j]["kickboard"] == '"SINGSING"'):
                    choice_month[3] += 1
                
        except:
            continue
    cnt += 1

# print(choice_month)

for i in brands:
    total += i

brs = {
    'GCOOTER': brands[0],
    'SWING': brands[1],
    'BEAM': brands[2],
    'SINGSING': brands[3],
}

# 지도에 사진 위치 마커
report_map = folium.Map(location=[37.5662952,126.9779451], tiles='cartodbpositron', zoom_start=12, min_zoom = 12)

for i in range(len(brand_name)):
    if(brand_name[i] == "GCOOTER"):
        folium.Marker([latitudes[i],longitudes[i]],
                    popup="GCOOTER",
                    tooltip="GCOOTER", 
                    icon=folium.Icon('green', icon='fa-solid fa-g', prefix='fa'),
                    ).add_to(report_map)
    elif(brand_name[i] == "SWING"):
        folium.Marker([latitudes[i],longitudes[i]],
                    popup="SWING",
                    tooltip="SWING", 
                    icon=folium.Icon('black', icon='fa-solid fa-s', prefix='fa'),
                    ).add_to(report_map)
    elif(brand_name[i] == "BEAM"):
        folium.Marker([latitudes[i],longitudes[i]],
                    popup="BEAM",
                    tooltip="BEAM", 
                    icon=folium.Icon('purple', icon='fa-solid fa-b', prefix='fa'),
                    ).add_to(report_map)
    elif(brand_name[i] == "SINGSING"):
        folium.Marker([latitudes[i],longitudes[i]],
                    popup="SINGSING",
                    tooltip="SINGSING", 
                    icon=folium.Icon('orange', icon='fa-solid fa-s', prefix='fa'),
                    ).add_to(report_map)

# html 코드 추가
template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
""" + \
"""
<div class='legend-title'>Status</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span class="brand-color" style='background:green;opacity:0.7;'></span><b>GCOOTER</b><span class="tab">&#9;</span>%d</li> 
    <li><span class="brand-color" style='background:black;opacity:0.7;'></span><b>SWING</b><span class="tab">&#9;&#9;</span>%d</li>
    <li><span class="brand-color" style='background:purple;opacity:0.7;'></span><b>BEAM</b><span class="tab">&#9;&#9;</span>%d</li>
    <li><span class="brand-color" style='background:orange;opacity:0.7;'></span><b>SINGSING</b><span class="tab">&#9;</span>%d</li>
    <li><span class="brand-color" style='background:white;opacity:0;'></span><b>Total</b><span class="tab">&#9;&#9;</span><b>%d</b></li>

  </ul>
</div>
</div>
""" % (brands[0], brands[1], brands[2], brands[3], total) + \
""" 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span.brand-color {
    display: block;
    float: left;
    height: 16px;
    width: 16px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .tab { white-space: pre; }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)
report_map.get_root().add_child(macro)
report_map.save('index.html')


# 년별 신고 횟수 막대 그래프
ax = plt.subplot(2, 1, 1,)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=30)
plt.bar(range(len(months)), months)
plt.ylabel("Number of reports")
plt.title('Reports in '+year, loc='right', pad=5)

# 월별 신고 횟수 막대 그래프
colors = ['#009933', '#333333', '#330099', '#FFCC33']
ax = plt.subplot(2, 1, 2)
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(labels, rotation=30)
plt.bar(range(len(choice_month)), choice_month, color=colors)
plt.ylabel("Number of reports")
plt.title('Reports in '+year+'-' + choice + '   Total : ' + str(sum(choice_month)), loc='right', pad=5)
plt.tight_layout()
# plt.show()
plt.savefig('bar_chart.png')


# 브랜드 비율 - 원형 차트
plt.figure(figsize=(6, 6))
# plt.pie로 생기는 요소를 다음처럼 리턴하여 값을 저장해두고 
patches, texts, autotexts = plt.pie(
    labels=labels,      # label 
    labeldistance=1.1,  # label이 파이로부터 얼마나 떨어지는가, 1일경우 딱 붙어있음. 
    x = brands,         # 값
    explode=(0.1, 0.1, 0.1, 0.1), ##pie가 튀어나오는지 정해줌  
    # startangle=90,## 어디에서 시작할지, 정해줌  
    shadow=True, ##그림자 
    counterclock=False, ## 시계방향으로 가는지, 시계 반대 방향으로 가는지 정해줌 
    autopct='%1.1f%%', ## pi 위에 표시될 글자 형태, 또한 알아서 %로 변환해서 알려줌 
    # pctdistance=0.7, ## pct가 radius 기준으로 어디쯤에 위치할지 정함 
    colors=['#009933', '#333333', '#330099', '#FFCC33'],
)

## 도넛처럼 만들기
centre_circle = plt.Circle((0,0),0.50,color='white')
plt.gca().add_artist(centre_circle)
## pie 위의 텍스트를 다른 색으로 변경해주기 
for t in autotexts:
    t.set_color("white")
    t.set_fontsize(10)
plt.title('Reports in '+year+'   Total : ' + str(sum(brands)), loc='center', pad=5)
# plt.show()
plt.savefig('pie_chart.png')