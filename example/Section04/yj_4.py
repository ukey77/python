# 3
# No = int(input('4자리 사원번호를 입력>>'))
# last = No % 10 >=5

# print('근무시간은 {}입니다'.format('오전' if last else '오후'))


#4
# no = int(input('라면의 개수를 입력>>'))
# box = no//20
# rest = no%20 > 0

# print('{}의 라면을 담으려면 {}박스가 필요합니다.'.format(no, box +1 if rest else box))

#5

ko = int(input('국어점수를 입력>>'))
En = int(input('영어점수를 입력>>'))
Ma = int(input('수학점수를 입력>>'))
avg = (ko+En+Ma)//3

print('평균은 {}점이고 결과는 [{}]입니다'.format(avg, '합격' if avg >= 80 else '불합격'))