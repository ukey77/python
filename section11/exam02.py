#2
""" 
키(Key)가 과목명, 값(value)이 점수인 marks 딕셔너리
해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average()함수 구현

함수 정의
- 반환값 : 평균
- 함수이름 : get_average()
- 매개변수 : 딕셔너리 marks

"""

# T
def get_average(marks:dict)->float:
  total=0
  for key in marks:
    total+=marks[key]
  return total / len(marks)
  
marks={'국어':90,'영어':80,'수학':85}
avg = get_average(marks)
print(f'평균은 {avg}점입니다.')



""" 
#해설
def get_average(marks):
    total = 0   
    for subject in marks:
        total += marks[subject]
    average = total / len(marks)
    return average

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print(f'평균은 {average}점입니다.')
"""
