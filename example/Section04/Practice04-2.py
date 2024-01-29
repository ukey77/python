# times = int(input('초를 입력하세요 >>> '))
# hour = times // 3600
# minute = times % 3600 // 60
# second = times % 60
# print('변환 결과는 {}시간 {}분 {}초입니다.'.format(hour, minute, second))


#  임의의 초를 입력받아 시/분/초 로 변환하여 출력

inp = int(input('초를 입력하세요 >>'))
hour = inp//3600
min = inp%3600//60
sec = inp%60

print('변환 결과는 {}시간 {}분 {}초입니다.'.format(hour, min, sec))

""" 
초를 3600으로 나눈 몫이 시간
초를 3600으로 나눈 나머지를 60으로 나눈 몫이 분
초를 60으로 나눈 나머지가 초
"""