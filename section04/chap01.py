""" 
연산자와 우선순위
"""

""" 
total = 0
total = total + 1
total = total + 1
total = total + 1
total = total + 1
total = total + 1
total += number
"""

# print( 5 > 10)
# result = 5 > 10
# print(result)
# result = 5 <= 10
# print(result)
# result = 5 == 10
# print(result)

# 논리 연산
res1 = 5 == 10
res2 = 5 <= 10
 
print(res1,res2)

result = res1 and res2
print(result)

result = res1 or res2
print(result)

result = not res2
print(result)

#1
hi = int(input('10~99사이의 정수를 입력 >>'))
ten = hi // 10
one = hi % 10
print(f'십의자리는 {ten} 일의 자리는 {one}')

""" 
1 byte = 8 bit
0 => 0000 0000
1 => 0000 0001
2 => 0000 0010
3 => 0000 0011
4 => 0000 0100
5 => 0000 0101
6 => 0000 0110
7 => 0000 0111
8 => 0000 1000
9 => 0000 1001
10 => 0000 1010
11 => 0000 1011
12 => 0000 1100
13 => 0000 1101
14 => 0000 1110
15 => 0000 1111
"""
# 비트연산자 : & , | , ^ , ~ , << , >>, >>> (and, or, elxclusive or, not, ..)

""" 
  0011
& 0100
======
  0000
  0111

  0011
^ 0110
======
  0101
  
둘다 1이여야 0을 출력


~ 0011 -> 1100


shift 연산 : 비트를 왼쪽/오른쪽 방향으로 이동
result = 3 << 2  ==> 3을 왼쪽으로 2비트 이동시킴
result = 0011 << 2
result = 1100

비트단위로 연산을 하다보니 속도가 빨라서 하게됨 ?


"""