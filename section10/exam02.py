#2
""" 
사업자 번호 : 숫자3자리-숫자2자리-숫자5자리
1. 전체 글자수를 점검
2. 모든 하이픈(-)의 위치가 올바른지 점검
3. 하이픈(-)을 제외하면 모두 숫자인지 점검
"""
# correct1=False
# correct2=False
# correct3=False

comp_num = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')

correct1 = True if len(comp_num)==12 else False

correct2 = True if comp_num[3]=='-'and comp_num[6]=='-' else False

temp = comp_num.replace('-','')
correct3 = temp.isdecimal()

if correct1 and correct2 and correct3:
  print(' 올바른 형식입니다.')
else:
  print('올바른 형식이 아닙니다.')


# 해설
n=input('사업자등록번호를 입력하세요 (예: 123-45-67890)>>>')

c1=(n.find('-')==3)
c2=(n.find('-',4)==6)
c3=(len(n)==12)
c4=(n.replace('-','').isdecimal)

if c1 and c2 and c3 and c4:
  print('올바른 형식입니다.')
else:
  print('올바른 형식이 아닙니다.')
