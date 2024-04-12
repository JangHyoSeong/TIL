import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 동적인 페이지는 정상적으로 가져올 수 없다 -> 구글은 안됨
    # response = requests.get(url)
    # print(response.text)

    # 따라서 동적인 컨텐츠를 가져오려면 selenium 사용
    # 크롬 브라우저가 열리고, 동적인 내용이 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다
    html = driver.page_source
    # 문자열 형태
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')

    # 보기좋게 출력
    # print(soup.prettify())

    # 파일로 출력
    # with open("soup.txt", "w", encoding="utf-8") as file:
    #     file.write(soup.prettify())

    # 검색 결과 개수는 result-stats라는 id를 사용
    result_stats = soup.select_one("#result-stats")
    # print(result_stats)

    # 각 게시물 가져오기
    # 공통적으로 div태그 + g클래스를 사용함
    g_list = soup.select('div.g')
    for g in g_list:
        # 요소 안에서 LC2-1b MBeu0 DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")

        # 요소가 존재 한다면 출력
        if title is not None:
            print('제목 = ', title.text)

get_data('탕수육')
