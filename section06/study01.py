""" 
#1
num = int(input('정수를 입력하세요 >>> '))
i = 1
while i<=num:
  print(f'{i}번째')
  i+=1
print('-----------------------')


# 예제1
n = 10
while n>=1:
  print(f'{n}번째')
  n-=1

# 예제2
my_list = []

n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n != 0:
  my_list.append(n)
  n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
print(my_list)


# a가 0보다 같거나 크면 실행 작으면 정지
a = int(input('a : '))

while a>=0:
  print('실행')
  a = int(input('a : '))
  
# e또는 E가 입력될때 까지 반복하기
txt = input('e 또는 E가 입력할때까지 반복>>')
while txt != 'e' and txt !='E':
  txt = input('e또는 E입력시 종료')
print('종료')
 


#1 

num = int(input('정수를 입력하세요 >>> '))

if num <= 0:
  print('잘못된 입력입니다')
else:
  n=0
  while n<=num:
    print(f'{n}번째 Hello')
    n+=1
    
"""

""" 
#2 1부터 100사이의 모든 정수 중에서 7의 배수만 출력


i = 1
n = i % 7

while i<=100:
  
  if not(n):
    print(i)
  i+=1
  
   """
   
   
   
""" #3 : 커피1잔 300원 

coffee = 0
money = int(input('자판기에 얼마를 넣을까요 >>> '))

while money >= 300:
  coffee += 1
  money -= 300
  print(f'커피 {coffee}잔, 잔돈{money}원') """
  
"""  #4 사용자로부터 0~9 정수 입력받음 / 입력한 정수가 5개가 될때까지 입력받도록
  
li = []

while len(li) < 5:
  n = int(input('정수 입력 >>> '))
  li.append(n)
print('모두 입력되었습니다')
print(li)
 """
"""  
#5 1~100 사이의 모든 정수를 한 줄에 10개씩 출력

n = 1
while n <= 100:
    if n % 10 == 0:
        print(n) #출력후에 새로운 줄로 넘어감
    else:
        print(n, end='\t') #탭으로 끝나게함
    n += 1
 """
 
"""  
#6 전체 구구단 출력


    
n = 1
while n <= 9: #n이 9가 될때까지 반복
  dan =2 
  while dan <= 9: #dan이 9가 될때까지 반복
    print(f'{dan}X{n}={dan*n}',end='\t') #tab으로 끝나는데?
    dan += 1 #dan은 1씩 증가
  print()#dan이 마무리 될때마다 줄바꿈
  n += 1 """
  
  # 1~100 이하 짝수 모두 출력
  
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1

