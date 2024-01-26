# 02_PJT

## 도전과제 1번 후기

### 새로 배운 내용
- numpy, pandas, matplotlib 사용법을 배울 수 있었다
- 데이터 관리 및 필터링 방법을 알 수 있었다
- csv 파일 등, 데이터를 파이썬으로 관리하는 방법을 알 수 있었다

```python
# CSV 파일 경로
csv_path = "data/NFLX.csv"

# CSV 파일 읽어오기
df = pd.read_csv(csv_path, usecols=range(5))
```
---
### 어려웠던 내용
- 월별로 그룹화 하는 것이 어려워서 좀 헤맸다
  - 이를 응용하면 인덱스번호, 남녀 성별, 학년, 반으로도 그룹화를 할 수 있을 듯하다.
  - 두 개 이상의 기준으로 그룹화 하는 방법에 대해서 따로 공부해야겠다고 생각했다.
- pandas로 dataframe을 관리하는 것이 익숙하지 않아서 힘들었다

---
### 느낀점
- SQL로 DB를 관리하는 것은 이전에 조금 해보아서 알고 있었는데, 파이썬 자체에서도 라이브러리를 통해 관리할 수 있다는 것이 신기했다.
- 구글링을 하면서 찾아보니 많은 기능을 확인할 수 있었는데, 앞으로도 데이터를 관리할 일이 있다면 더 많은 기능을 사용해보고 싶었다.

---
## 도전과제 2번 후기

### 새로 배운 내용
- URL을 통한 요청 방법
  - endpoint와 query는 '?'로 연결 및 구분
  - 각각의 query는 '&'로 연결
  - `http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType={query_type}`
  - 혹은 params를 사용하여 담을수도 있음
```python
URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

params = {
    'ttbkey': '',
    'QueryType': 'ItemNewAll',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
}

response = requests.get(URL, params=params).json()
pprint(response['item'])
```
- query를 작성해서 필요한 정보를 가져온다는 사실을 처음 알게 되었음
  - 응용하면, 사용자에게 query 를 입력받아 필터링을 통해 값을 받아올 수도 있을거라 생각됨
  - 파라미터는 [파라미터 key]=[파라미터 Value]가 한세트이며, 공식문서에 명시된 key를 정확히(대소문자 구분)사용해야 한다.


### 어려웠던 내용
- 원하는 정보만을 가져오기 위해 쿼리를 작성할 때, 조건이 복잡해지면 작성하기 어려웠다.
- 특히나 한번의 호출로 값을 추출한 뒤, 그 값을 적절히 처리한 뒤 다른 값을 추출하는 것이 어려웠다.