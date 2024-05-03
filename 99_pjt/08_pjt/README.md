# 프로젝트 8회차

## 장효승 8회차 후기

### 배운 점
- django와 javascript를 본격적으로 같이 사용하는 방법을 연습할 수 있었다.
- django view의 return으로 json파일만을 제공받아, 이를 통해 화면을 구성하는 방법을 새롭게 알 수 있었다.
- 또한 비동기 요청을 통해 template에서 실시간으로 화면을 바꾸는 방법을 연습할 수 있었다.

### 어려웠던 점
- django의 view에서 json파일로 변환하는 방법이 조금 헷갈려서 많이 해맸다.
- 특히, vue를 사용해서 필터링을 구현하려 했는데, 반응형 변수와 django의 response를 어떻게 적절히 사용해야 할지 헷갈렸다.
- 아직까지 django를 통해 json파일을 만드는 법이 익숙하지 않았다

### 느낀 점
- 확실히 json파일을 서버측에서 제공받아 화면을 구성하는 방법이 편했다. 특히 비동기 방식은 익숙해져야 겠다고 생각했다.
- 앞으로도 프로젝트를 정해진 표준에 맞춰 제대로 구성하는 방법을 연습해야겠다고 생각했다.


### 김동현 8회차 후기
- 어려웠던 부분 : 영화 장르 필터링
	- 장르와 영화에 맞는 영화 데이터 목록 필터링 후 출력
    - view.py에서 영화 데이터를 필터링하는 어려움이 있었음
- 해결
    if genre_id:
        movies = Movie.objects.filter(genres__id=genre_id)
        movies_data = [{'title': movie.title} for movie in movies]
        return JsonResponse(movies_data, safe=False)

- 느낀 점
    - Json 파일을 필터링하는 과정이 익숙하지 않아 어려웠다
    - 비동기 방식도 익숙해져야겠다