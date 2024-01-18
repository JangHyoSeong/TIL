# 파이썬 가상환경 설정

### 써드파티 라이브러리 다운받을 때 꼭 해야하는 것
1. 공식 문서 보기
2. 릴리즈 히스토리 확인하기


---
### requirements.txt
- 프로젝트 시작할때 requirements.txt 파일을 만들고
- 프로젝트에서 사용하는 라이브러리의 버전을 모두 기록해야함
- pip freeze > requirements.txt 
- --> 컴퓨터에 설치되어있는 모든 패키지가 표시됨

## 가상환경 설정
- 하는 이유 : 현재 프로젝트를 위한 환경 설정을 위해

### 하는 법
- 대체로 폴더명은 venv로 설정
- bash에 `python -m venv venv` 입력 : venv 폴더 생성
- `python -m venv {폴더명}`
- `source venv/Scripts/activate`  : 가상환경 활성화
- 이걸 하고나면 패키지가 전부 초기화됨 
- 이후에 pip install로 필요한 패키지만 설치
- pip list : 패키지 목록 확인
- pip freeze > requirements.txt : 설치된 패키지 목록 txt파일로 작성
- deactivate : 가상환경 종료
- pip install -r requirements.txt : txt파일에 작성된 목록만 설치