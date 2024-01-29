#1
test= int(input('점수를 입력하세요 >>>'))
grade = 'F'


if test >= 90: 
  grade = 'A'
elif test >= 80: 
  grade = 'B'
elif test >= 70: 
  grade = 'C'
elif test >= 60: 
  grade = 'D'
else:
  grade
  
print(f'점수는 {test}점이고, 학점은 {grade}학점입니다')
  
print('------------------------------')
#2
itg = int(input('정수를 입력하세요 >>>'))
dv = itg%3
result = '아닙니다'
if dv == 0:
  result = '입니다'
else:
  result
  
print(f'{itg}은 3의 배수 {result}')

print('------------------------------')
#3 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요. ★★

num1 = int(input('정수1 입력>>>'))
num2 = int(input('정수2 입력>>>'))
num3 = int(input('정수3 입력>>>'))

max_v = num1

if max_v < num2:
  max_v = num2

if max_v < num3:
  max_v = num3
  
print(f'가장 큰 수는 {max_v}입니다')

print('------------------------------')
#4
car = input('차량번호를 입력하세요 >>>')
num = int(car[-1])
result = num % 2 
ps =  '운행불가능' if result else '운행가능'

print(f"차량번호 '{car}'는 오늘 {ps}입니다")


""" 
1. 문자열 안에서 작은따옴표, 2 큰따옴표 넣기
(1) " ' ' " 
(2) ' " " '
"""
number = '123가1234'
name = f'\'{number}\''
name = f'\"{number}\"'

name = f' " " '
name = f" ' ' "
