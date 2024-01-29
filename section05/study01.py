#1
score = int(input('점수를 입력하세요 >>> '))
level = 'A'
if score >= 90:
  level
elif score >= 80:
  level = 'B'
elif score >= 70:
  level = 'C'
elif score >= 60:
  level = 'D'
else:
  level = 'F'
  
print(f'점수는 {score}점이고, 학점은 {level}학점입니다.')

#2
num = int(input('정수를 입력하세요 >>> '))
devide = num % 3
result = '입니다.'

if not(devide):
  result
else:
  result = '가 아닙니다.'
  
print(f'{num}은 3의 배수{result}')

#3
num1 = int(input('정수 1입력 >>> '))
num2 = int(input('정수 2입력 >>> '))
num3 = int(input('정수 3입력 >>> '))

max_n = num1

if max_n < num2:
  max_n = num2
# num1을 기준으로 잡고 num2와 비교한후 더 큰수를 max에 넣기
if max_n < num3:
  max_n = num3
# 비교결과를 num3과 한번더 비교하여 더 큰수를 max에 넣기

print(f'가장 큰 수는 {max_n}입니다.')

#4
num = input('차량번호를 입력하세요 >>> ')
car = int(num[-1]) % 2
bool = '운행가능'

if not(car):
  bool
else:
  bool = '운행불가능'

print(f"차량번호 '{num}'는 오늘 {bool}입니다")

