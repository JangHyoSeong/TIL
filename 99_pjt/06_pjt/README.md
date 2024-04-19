# 06주차 Project

## 김동현 소감

### 협업 GIT
- PUSH하려면
내 branch에서 git add . + git commit 해준 뒤,
git switch master로 공용 branch로 간 뒤,
git merge 내 branch 해서 github로 push한다

- PULL하려면
내 branch에서 git add . + git commit 해준 뒤,
git switch master로 공용 branch로 간 뒤,
git pull origin master해서
switch로 다시 돌아온 뒤 merge한다

### 어려운 문장
- base.html에서
<!-- 로그인이 되어 있다면 -->
{% if request.user.is_authenticated %} 

- index.html에서
<!-- 사용자가 좋아요를 누른 리스트에 들어있으면 아래 문장 실행 -->
{% if request.user in movie.like_users.all %} 

- 로그아웃 기능도 form으로 작성
<!-- <form action="{% url "accounts:logout" %}" method='POST'> -->

## 장효승 소감

### 새로 배운 점
- git을 통한 협업하는 법을 알 수 있었다.
- 원격 저장소를 경유하여 merge하는 것은 익숙하지 않아 실수가 많았는데 이번 프로젝트를 통해 제대로 알 수 있었다.
- django 전체 내용에 대해 복습 할 수 있었다.

### 어려웠던 점
- 서로 같은 부분을 편집하면 conflict가 생겨서 불편했다.
- 아직까지 협업을 효율적으로 하기 힘들었다

### 느낀점
- 협업을 통해 파트를 나누어 진행하니 프로젝트 시간을 줄일 수 있었다.
- django 배운 내용을 제대로 숙지하고 있었다고 생각했는데, 다시 돌아보니 까먹은 내용이 많았다. 더 열심히 공부해야겠다고 생각했다.