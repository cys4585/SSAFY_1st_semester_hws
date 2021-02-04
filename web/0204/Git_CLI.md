# CLI

​	Command Line Interface



## ls

- 현재 작업중인 폴더에 존재하는 파일 혹은 폴더 목록

ls -a 

- 숨김 파일 목록도 함께 확인할 수 있다.

ls -al

- 더 상세한 정보를 확인할 수 있다.



## cd

- change directory
- 작업 위치 옮기기
- cd {folder name}
  - 하위 폴더 중 name 폴더로 이동
- cd ..
  - 상위 폴더로 이동



## mkdir

- make directory
- 폴더 만들기
- mkdir {folder name}



## rm

- rm {file name}
  - 특정 파일을 삭제하기
- rm -r {folder name}
  - 폴더 삭제하기



## git stash

- git add로 관리되고 잇는 staging area에 있는 변동사항을 가상 공간에 따로 빼 둘수가 있다.

```bash
# 현재 수정사항 가상공간에 빼두기
$ git stash

# 가상공간에 있던 작업현황 다시 가져오기 + 가상공간에서 제거
$ git stash pop

# 가상곤간에 있던 작업현황 다시 가져오기 + 가상공간은 유지
$ git stash apply

# 가상 저장공간 확인
$ git stash list

# 가상 저장공간 제거
# First in Last Out
$ git stash drop
```



## code {folder or file name}

- code vscode