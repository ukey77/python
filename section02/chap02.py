""" 
Collection
-list
-tuple
-set
-dictionary
 """

li = [] #비어있는 리스트를 생성
li = [1,2,3,4,5]
print(li)
li.append(6)
print(li)
li.remove(1)


tp = tuple(li)
tp = (1,2,3,4,5,)

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)

di = dict() # 빈 딕셔너리 생성
di ={
  "tomato":"토마토",
  "banana":"바나나",
  "apple":"사과"
  }
print(di)
di['orange'] ='오렌지'
print(di)
di['apple'] = '애플'
print(di)
print(di['tomato'])

some_fruit = di['banana']
print(some_fruit)
some_fruit = di['apple']
print(some_fruit)

di.setdefault()

di.update(tomato='토마토마')
print(di)
val = di.pop('tomato')
print(val)
print(di)