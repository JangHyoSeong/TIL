# 자동으로 .git 폴더 삭제해주는 코드
# 현재 폴더를 기준으로 모든 폴더를 조사하여서
# .git 폴더를 삭제한다
# 단 최상위 폴더(코드가 실행된 위치의 .git)제외

# 운영체제와 상호작용이 가능한 모듈
import os
import subprocess

# get current working directory

# 현재 디렉토리를 return
current_dir = os.getcwd()

# os.walk() : generator 라는 객체(순회 가능함)
# 현재 폴더 및 모든 하위폴더를 반복

for foldername, subfolders, filenames in os.walk(current_dir):
    # print(foldername, 'fn')
    # print(subfolders, 'sf')
    # print(filenames, 'file')
    if '.git' in subfolders:
        # root 디렉토리는 제외하려면
        if foldername == current_dir:
            continue
        # 그 외 모든 폴더에서 .git 삭제
        # 삭제하려는 .git 폴더의 위치를 변수로 저장해야함
        git_folder_path = os.path.join(foldername, '.git')
        # 경로 : 'folder' + '.git' -> folder/.git
        subprocess.run(['rm', '-rf', git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다')



# 디렉토리 이동
# os.chdir('python_ws_6_1/')
