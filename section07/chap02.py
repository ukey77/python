""" 
비시퀀스와 for반복문
"""

comp = {'현대','기아','쌍용','벤쯔'} # 초기화된 set
for s in comp:
  print(s)
  
di = {
  'flower':'꽃',
  'car':'자동차',
  'cup':'컵',
  'object':'객체'
}

for s in di:
  print(f'{s} : {di[s]}')
  di.get(s) # di[s]
