#1 

inp = int(input('임의의 두자리 정수 입력>>'))
print(f'십의 자리는 : {inp//10}, 일의 자리는 : {inp%10}입니다')

#2 
t = int(input('초를 입력하세요 >>'))
h = t // 3600
m = t % 3600 // 60
s = t % 60

print(f'변환 결과는 {h}시간 {m}분 {s}초 입니다.')

#3 
num = int(input('4자리 사원번호를 입력하세요>>'))
last = num % 10
print('근무 시간은 {}입니다'.format('오전' if last >= 5 else '오후'))

#4
ra = int(input('라면의 개수를 입력하세요>>'))
box = ra // 20 
rest = box+1 if ra % 10 > 0 else box
print(f'{ra}개의 라면을 담으려면 {rest}박스가 필요합니다')

#5
ko = int(input('국어 점수를 입력하세요 >>'))
en = int(input('영어 점수를 입력하세요 >>'))
ma = int(input('수학 점수를 입력하세요 >>'))
avg = (ko+en+ma) // 3.0
result = '합격' if avg >= 80 else '불합격'
print(f'평균은{avg:.2f}점 이고, 결과는 {result}')\
  
  #  결과는 최대한 간략하게 !