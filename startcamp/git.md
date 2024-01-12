### git add, commit

---

### git add

```bash
git add [디렉토리] #폴더 하나 올리기
git add [파일이름] #파일 하나만 올리기
git add . #모두 올리기
```

---

### git commit

```bash
git commit -m "[commit message]"  #커밋, 큰 따옴표 안에 커밋 메세지 작성
```

- add를 하면 staging area에 저장됨
- commit : 버전을 하나 새로 만드는 것. repository에 저장 (작업 폴더 내 .git에 저장

```bash
commit은 언제 하는 것이 좋은가?
- 기능 하나가 완성되었을 때 (ex : 커밋 메세지에 “로그인 기능 구현”)
이렇게 해야 유지보수, 협업에 용이함

- 어쩔 수 없이 저장해야 할 때 (ex : 하던거 그만두고 딴거할 때)
```

```bash
git commit --amend #가장 최근에 한 commit 메세지 수정
```

- 이 명령어를 사용하면 vi라는 터미널이 열림
- 커밋 메세지 수정 가능
- Insert 버튼을 통해 수정모드로 변경, Esc 누르면 읽기모드로 변경, 읽기모드에서 :wq를 통해 종료

---

### **git status**

```bash
git status #git 상태를 알려줌
git log    #git 로그를 알려줌, 작성자, 날짜 등
git log --oneline #한 줄로 커밋 로그를 알려줌, 자동으로 나오는 작성자, 시간은 안나옴
```


**git status 가 무엇인가?**

- git status는 자주 사용하자
  - working tree clean이 출력되면 문제없음
  - 현재 커밋과 작업 폴더가 수정사항이 생기면 알려줌
  - 혹은 현재 staging area(git add가 저장되는 영역)과 다르면 알려줌
      

