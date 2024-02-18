""" 
파일입출력

파일 종류 : 텍스트파일 (text file), 바이너리 파일(Binary 파일)
파일 입력 : 파일로부터 데이터를 읽는 것 (Read File, Load)
파일 출력 : 데이터를 파일에 저장하는 것 (Write File, Save)

파일을 연다 (읽기 또는 쓰기 모드중 한가지 방법으로만 열수 있다)
파일을 쓴다 (또는 파일로부터 읽는다)
파일을 닫는다

[File Mode]

3중하나
r : 읽기 모드
w : 쓰기 모드
a : 추가 모드

2중 하나
t : 텍스트 모드
b : 바이너리 모드

"""
# path : file 위치 + 파일명
#파일 입출력
file = open('파일명','rt')
file.write('data')
file.write('data')
file.write('data')
file.write('data')
file.write('data')
file.close()

#파일 입력
file=open('파일명','r')
file.read()
file.close()

with open('파일명','r') as file:
  file.read()
# with문을 빠져나오면 file.close()를 자동으로 해줌

  
  
