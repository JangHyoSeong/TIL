# CLI (Command Line Interface)

- cmd를 통해 조작하는 UI를 말함 <-> GUI<br><br>


## 왜 CLI를 사용하는가?

- 수 많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공함
  - GUI는 CLI보다 성능을 상대적으로 많이 소모

---

## CLI 사용법

> **파일 생성시 한글, 공백, 특수문자( _ - 제외) 절대금지**
- 상대경로를 사용
  - 현재 위치 :  .
  - 상위 폴더 :  ..
- ls : 현재 디렉토리의 파일/폴더 목록
- touch : 파일 생성 (ex : touch test.md) (touch [파일경로]/[파일 이름])
- mkdir : 폴더 생성 (ex : mkdir test) (mkdir [경로]/[폴더이름])
- rm : 제거
  - 폴더를 지울 때 : rm -r [폴더이름]
  - 파일을 지울 때 : rm [파일이름]
- cd : 작업 위치 이동
- start : 파일/폴더 열기 (ex : start [경로]/[파일이름])
- mv : 파일 이동 ([이동할 대상] [이동할 위치]) (ex : )(이름 변경도 가능)
- vscode로 열기 : code (경로)
- vscode에서 터미널 열기 : ctrl + shift + \`