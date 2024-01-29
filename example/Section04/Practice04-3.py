no = int(input('4자리 사원번호를 입력하세요 >>> '))
last= no % 10
is_am = last >= 5
print('근무 시간은 {}입니다.'.format('오전' if is_am else '오후'))
