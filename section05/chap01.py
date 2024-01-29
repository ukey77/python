""" 
조건문 (if statement)
"""

num1 = 10
num2 = 5
if num1 == 10 and num2 == 5:
  print(num1)
  print(num2)

print('조건문 처리가 끝났습니다.')

print('---------------------------')


if num1 == 10:
  print(f'{num1}의 값은 10입니다')
else:
  print(f'{num1}의 값은 10이 아닙니다')

isOk = True
li = [] # 빈리스트
nothing = ''
num1 = 0

if isOk:
  print(isOk)
  
if li: #if문의 조건으로 사용될 수 있음, 빈리스트의 논리값은 False임
  print(li)
  
if(nothing): #빈 문자열의 논리값은 False임
  print(nothing)  

if(num1): #정수 0의 논리값은 False임
  print(num1)
  
# 복합 if문
num1 = 10
if num1==0:
  print('num1은 0입니다')
elif num1==1:
  print('num1은 1입니다')
else:
  print('num1은 5이상입니다')

print('---------------------------')

if num1==16:
  if num2==5:
    print(num1)
    print(num2)
  else:
    print('num1은 10이고, num2는 5가 아닙니다')
else:
  print('num1은 10이 아닙니다')