
total=10 # 전역변수

def my_func(num1:int):
  print(f'total = {total}') #전역변수 total
  print(num1)


def my_func2():
  #total=20 #(단독기재) my_func2의 지역변수로써의 total (전역변수와는 무관)
  global total #전역변수 total을 이 함수안에서 선언함
  total=20 #전역변수 total의 값을 변경
  number=10 #my_func2의 지역변수
  print(total)


my_func(2)
my_func2()                                              
print(f'total = {total}')
number=10
print(f'number={number}')

