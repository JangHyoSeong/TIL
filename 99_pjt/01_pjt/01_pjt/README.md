# 학습 내용


## 새로 배운 내용

- 파일 여는법 : data/book.json 파일을 연다, utf-8로
- utf-8 : 유니코드에서 한글 읽는 코드

```python
#파일 여는 법 예시
artist_json = open('data/artist.json', encoding='utf-8')
artist_dict = json.load(artist_json)
```

- json.load() : json파일을 파이썬에서 사용할 수 있도록 변환해주는 함수
- 깔끔하게 정렬하는 법
```python
sortedBookList = sorted(bookList, key = lambda x: x.get('priceSales',0), reverse=True) 
# bookList는 딕셔너리가 담겨있는 리스트
# bookList를 priceSales라는 key로 역방향(내림차순) 정렬한다는 뜻
```

## 어려웠던 내용

- json 파일에서 조건에 맞는 값을 추출하는 것이 힘들었다
  - 특히 json 파일이 여러개 얽혀있는 경우 코드 한 줄이 길어져서 가독성이 떨어졌다
  - 이를 해결하기 위해 방법을 생각해볼 예정
</br>

- 앞의 내용과 비슷하게, 적절한 변수명을 짓는 것이 어려웠다
  - 비슷한 변수명이 많다보니 헷갈리고 일관성이 없었다
  - 앞으로 많은 프로젝트를 경험하면서 해결할 예정

## 느낀점
- 지금까지 파이썬은 사용자가 직접 입력을 하는(input함수) 식으로 코딩을 해왔는데, 이렇게 json파일을 입력으로 사용하여 데이터를 처리하니까 재밌었다.
- 앞으로 기회가 된다면 더욱 더 큰 파일 규모의 데이터 처리를 해보고 싶다.