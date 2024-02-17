""" # 리스트 메소드 : 추가, 삽입, 삭제
li = [10,20,30] #리스트에 데이터를 추가하는 메소드
li.append(50)
li.append(40)
print(li)


li.insert(1,15) #두번째 요소에 값 15를 삽입
print(li)

print(li.extend([10,20,30])) # 확장
print(li)


value = li.pop()
print(value)

li.remove(10)
print(li) """

# set method
s1={10,20,30}
s2=set(20,30,40)

#교집합 s1 & s2
s3 = s1.intersection(s2)
print(s3)
s4 = s1 & s2
print(s4)

#합집합 


#차집합