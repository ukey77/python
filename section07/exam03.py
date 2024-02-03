#3 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 그 숫자만큼 과일 이름을 입력받아
# basket이라는 리스트에 저장 하는 프로그램을 구현

""" 
basket = []
num = int(input('몇 개의 과일을 보관할까요? >>> '))
for n in range(num):
  fr = input(f'{n+1}번째 과일으르 입력하세요 >>>')
  basket.append(fr)
print(basket)

"""
  
num = int(input('몇 개의 과일을 보관할까요? >>> '))
basket = set()

while len(basket)<num:
  fr = input(f'{len(basket)+1}번째 과일을 입력하세요 >>>')
  basket.add(fr)
   
print(basket)