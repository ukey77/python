#3
""" 
입력된 데이터를 각각 name과 score라는 변수에 저장하는 프로그램
학생의 이름과 점수를 입력하세요 >>> 김철수,85
이름은 김철수 이고, 점수는 85점입니다.
"""
school=input('학생의 이름과 점수를 입력하세요 >>>')
tem=school.split(',')
name=tem[0]
score=tem[1]
print(f'이름은 {name}이고, 점수는{score}입니다')