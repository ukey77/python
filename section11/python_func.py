""" 
파이썬의 특별한 함수 스타일
"""

# 코드의 생략
def pass_func():
  ... # =pass / 구상중이다
  
  
# 가변 매개변수
def show(*vals:int, horiz:int=1): 
  print(vals)
  for n in vals:
    if horiz==1:
      print(n,end='\t')
    else:
      print(n)
  print()
  
show(1,2,3,4,5,horiz=5)
show(1,2,3)

#2
def greet(message:str, temp:int, count:int=1): # 디폴트값줄때는 변수를 마지막에 작성
  for n in range(count):
    print(message,temp)

greet('하이',1)
greet('3번반복',3,count=3)
greet('5번반복',5,count=5)


print('---------------------')

def my_divmod(num1:int,num2:int):
  mok=num1//num2
  nam=num1%num2
  return mok, nam

mok,nam=divmod(10,3)
values=divmod(10,3)

print(mok,nam)
print(values)


mok,nam=my_divmod(10,3)
print(mok,nam)

values=my_divmod(10,3)
print(values[0],values[1])









