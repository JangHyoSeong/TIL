from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
import base64
from matplotlib.dates import DateFormatter, MonthLocator


def problem1(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    df = pd.DataFrame(df)
    data = df.to_html(index=False)
    context = {
        'df' : df,
        'data' : data,
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    # print(df)
    high = df['TempHighF']
    low = df['TempLowF']
    avg = df['TempAvgF']

    date = pd.to_datetime(df['Date'])

    plt.clf()

    plt.plot(date, high, label='High Temperature')
    plt.plot(date, avg, label='Average Temperature')
    plt.plot(date, low, label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(loc='lower center')
    plt.grid(True)

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()



    context = {
        'image' : f'data:image/png;base64, {img_base64}',
        'df' : df,
        
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):

    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)

    # Date를 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    # 온도 필드를 숫자 형식으로 변환
    df['TempHighF'] = pd.to_numeric(df['TempHighF'], errors='coerce')
    df['TempLowF'] = pd.to_numeric(df['TempLowF'], errors='coerce')
    df['TempAvgF'] = pd.to_numeric(df['TempAvgF'], errors='coerce')

    # 월별 평균 온도 계산을 위해 'YYYY-MM' 형태로 그룹화
    df['Year_Month'] = df['Date'].dt.to_period('M')

    # 월별 평균 온도 계산
    monthly_avg_temp = df.groupby('Year_Month').agg({'TempHighF': 'mean', 'TempLowF': 'mean', 'TempAvgF': 'mean'})

    plt.clf()

    # 월별 평균 온도 선 그래프 시각화
    plt.plot(monthly_avg_temp.index.astype(str), monthly_avg_temp['TempHighF'], label='High Temperature')
    plt.plot(monthly_avg_temp.index.astype(str), monthly_avg_temp['TempAvgF'], label='Average Temperature')
    plt.plot(monthly_avg_temp.index.astype(str), monthly_avg_temp['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xticks(monthly_avg_temp.index[1::6].astype(str))


    plt.legend(loc='lower right')
    plt.grid(True)

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'df': df,
    }
    return render(request, 'weathers/problem3.html', context)



def problem4(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)

    df['Events'] = df['Events'].apply(lambda x: 'No Events' if x.strip() == '' else x)
    # 각 행의 이벤트를 분리하여 개별적으로 처리
    events_list = df['Events'].str.split(', ')
    event_counts = {}
    for event in events_list:
        for e in event:
            # 이벤트의 양쪽 공백을 제거한 후에 처리
            e = e.strip()
            if e not in event_counts:
                event_counts[e] = 0
            event_counts[e] += 1

    # 이벤트 카운트를 기준으로 내림차순 정렬
    sorted_events = dict(sorted(event_counts.items(), key=lambda x: x[1], reverse=True))


    # 히스토그램 생성
    plt.clf()
    plt.bar(sorted_events.keys(), sorted_events.values())
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.xticks()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'df': df,
    }
    return render(request, 'weathers/problem4.html', context)