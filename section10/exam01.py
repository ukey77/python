#1
n=input('전화번호를 입력하세요 >>>')

start=n.index('-')+1
end=n.index('-',start)

print(start,end)
print(n[start:end]) #문자열 슬라이싱

# split 이용

li=n.split('-')
print(li)
print(li[1])