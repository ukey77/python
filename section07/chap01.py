# for

li = [10,20,30,50,80,100]
for num in li: # li에 있는 모든 아이템들을 num이라는 변수에 대입하면서 반복수행함
  print(num)
  
s = 'Hello Python'
for ch in s:
  print(ch)
    
li = ['파이썬','자바','C/C++','kotlin']
for s in li:
  print(s)

#
print(range(5)) # range(n) 0 ~ n-1까지 데이터 생성됨

li=list(range(5,10)) # range(s,e) s~e-1까지 데이터 생성됨
print(li)

li=list(range(1,10,2)) # range(start,end,step) start ~ end-1까지 step씩 건너뛰면서 데이터 생성
print(li)

for num in range(5):
  print(num,end='\t')

print()

for num in range(1,6):
  print(num,end='\t')

print()

for num in range(5): #반복횟수를 지정해야 될 때도 range()를 사용함
  print('Hello Python')
  
dan = int(input('구구단을 출력할 단수를 입력하세요 >>> '))
for num in range(1,10):
  print(f'{dan}X{num}={dan*num}')