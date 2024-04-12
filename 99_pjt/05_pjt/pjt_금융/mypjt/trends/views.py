from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def get_data_year(keyword):
    url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    result = soup.select_one('#result-stats').text
    return result

def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    result = soup.select_one('#result-stats').text
    return result

# Create your views here.
def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        keywords = Keyword.objects.all()
        form = KeywordForm()
    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()

    
    for keyword in keywords:
        
        search_result = get_data(keyword.name)
        result, dummy = search_result.split('개')
        numbers = re.findall(r'\d+', result)
        result = int(''.join(numbers))
        defaults = {
            'keyword' : keyword,
            'name' : keyword.name,
            'search_period' : 'all',
        }
        trend, created = Trend.objects.update_or_create(keyword=keyword, name=keyword.name, search_period = 'all', defaults={'result': result})
        # trend, created_trend = Trend.objects.update_or_create(result=result, search_period='all', defaults=defaults)
        # trend, created_trend = Trend.objects.update_or_create(name=keyword.name, result=result, search_period='all')
    
    trends = Trend.objects.filter(search_period='all')

    context = {
        'trends' : trends,
    }

    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    plt.switch_backend('Agg')
    trends = Trend.objects.all()
    # Pandas DataFrame 생성
    data = {
        'name': [trend.name for trend in trends],
        'result': [trend.result for trend in trends]
    }
    df = pd.DataFrame(data)
    
    # 히스토그램 그리기
    plt.clf()
    plt.bar(data['name'], data['result'], label='Trends')
    # 그래프 제목과 축 라벨 설정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(loc='upper right')
    
    # x축 눈금에 trend의 name 필드 사용
    # plt.xticks(range(len(df)), df['name'], rotation=45)
    
    # 그래프 이미지를 BytesIO 객체에 저장
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
   
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8').replace('\n', '')


    # 그래프 이미지를 템플릿으로 전달
    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'df' : df,
        }
    
    return render(request, 'trends/crawling_histogram.html', context)

def crawling_advanced(request):
    keywords = Keyword.objects.all()

    
    for keyword in keywords:
        
        search_result = get_data(keyword.name)
        result, dummy = search_result.split('개')
        numbers = re.findall(r'\d+', result)
        result = int(''.join(numbers))
        defaults = {
            'keyword' : keyword,
            'name' : keyword.name,
            'search_period' : 'year',
        }
        trend, created = Trend.objects.update_or_create(keyword=keyword, name=keyword.name, search_period = 'year', defaults={'result': result})
        # trend, created_trend = Trend.objects.update_or_create(result=result, search_period='all', defaults=defaults)
        # trend, created_trend = Trend.objects.update_or_create(name=keyword.name, result=result, search_period='all')
    
    trends = Trend.objects.filter(search_period='year')
    # Pandas DataFrame 생성
    data = {
        'name': [trend.name for trend in trends],
        'result': [trend.result for trend in trends]
    }
    df = pd.DataFrame(data)
    
    # 히스토그램 그리기
    plt.clf()
    plt.bar(data['name'], data['result'], label='Trends')
    # 그래프 제목과 축 라벨 설정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(loc='upper right')
    
    # x축 눈금에 trend의 name 필드 사용
    # plt.xticks(range(len(df)), df['name'], rotation=45)
    
    # 그래프 이미지를 BytesIO 객체에 저장
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
   
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8').replace('\n', '')


    # 그래프 이미지를 템플릿으로 전달
    context = {
        'image': f'data:image/png;base64, {img_base64}',
        'df' : df,
        }

    return render(request, 'trends/crawling_advanced.html', context)