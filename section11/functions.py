#사용자정의함수
""" 
print(), input(), len(),

함수 정의 : Define a function
함수의 호출 : Call a function

매개변수 : 함수의 입력값
반환값 : 함수의 출력값

1 매개변수O, 반환값 O
2 매개변수X, 반환값 O
3 매개변수O, 반환값 X
4 매개변수X, 반환값 X

"""
#ex 4
li=[1,2,3]
li.clear()


# 함수의 정의 
# 매개변수O, 반환값 X
# consumer function(method) , 소비형함수
def greet(message,count): # 매개변수는 없어도되고, 여러개여도 됨
  for n in range(count):
    print(message)


#매개변수O, 반환값 O
def add(num1:int, num2:int) -> int: # dateType 지정 -> 내뱉는것도 int지정
  return num1+num2

    
#매개변수X, 반환값 X
def say_hello():
  print('안녕하세요, 반값습니다+')

#매개변수X, 반환값 O
def get_pi():
  return 3.14


greet('안녕하세요',5)
greet('반갑습니다',5)
greet('안녕히',5)

num3=add(10,20)

num3=add(3,7)

num3=add(1.1,3.5)

num3=add(1.1,3)

num3=add('hi','bye')




#파라미터, 매개변수, 아규먼트(Argument),  인수, 인자 >>  다같은말임

