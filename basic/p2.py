# py 2. 단일 데이터 / 용법들

# 단일데이터( 단일 타입 )
# 문자열(연속이지만, 이쪽으로도 분류한다)
# 표기법
# '...', "...", '''...''', """..."""
# '''...''', """...""" 용도 : 여러줄표현, 구조유지, (여러줄)주석용
a = 'hi'
print(a)
a = "hi"
print(a)
# 혼용 표현
a = 'abcd"kkk"efg'
print(a)
# 이스케이프 문자로 동일 기호를 내부에서 사용 가능
a = 'abcd\'kkk\'efg'
print(a)
# 여러줄
a = """
asdasd
asdsdsksk
skksow
sksk
"""
print(a)
"""
여러줄 주석
"""

##################################################################
# 문자열 더하기 ( 이어 붙이기 ) <-> 문자열안에 문자열( 포멧팅 ) 
a = 'hellow'
b = 'lunch'
print(a+b)
# 문자열 반복
print('1'*10)
##################################################################

# 인덱싱 : indexing : 문자열에서 특정 문자를 획득하는 방식
#   -> 차원축소의 의미 
# 문법 : 변수명[ 인덱스(정방향or역방향 <= 가까운쪽 기준으로 정함) ]
a = '0123456789'
# 2를 출력
print( a[2] )
print( a[-8], '뒤에서 체크하면 머니까 가까운쪽으로 해결한다' )

# 슬라이싱 : 데이터에서 범위에 해당되는 데이터를 획득
#           -> 차원유지
# 문법 : 변수[ 시작인덱스:끝인덱스:step(짜르는 간격, 생략하면 1) ]
# a를 카피한다.
print( a[:])
# 1~8까지 출력
print(a[1:9:1])
# 뒤에 경계값을 포함 않됨
print( a[-1], a[1])
# a<= <b
print(a[1:-1])
print(a[1:-1:2])
##################################################################
ur1 = 'https://taegon.kim/wp-content/uploads/2018/05/image-5.png'
# 위의 이런 문자열의 파일명을 추출, 도메인 추출 등등 사용가능
print( a[:2], a[-2:])
##################################################################
# 멤버함수(문자열)
a = "0123456789"
# 문자열내에 특정 문자 개수
print('a라는 문자열의 2의 갯수', a.count('2') )
print('a라는 문자열의 A의 갯수', a.count('-A') ) # 없으면 0개 
# a라는 문자열에 "A"라는 문자가 존재하는가?
print('존재여부', a.count('A')>0)
print(a.index('2'))
# 에러, 없는 문자는 예외처리 해야한다.
# print(a.index'(A'))
print(a.find('2'))
print(a.find('A')) 
# 문자열에서 문자열 찾기는 count(), find()를 사용해라.
##################################################################
b = ','
# 조인
print(b.join(a) )
# 분해
print(b.join(a).split(b))
# 공백제거 
a = '   sdffs asdkljk asdlk     '
print('[%s]'%a.lstrip() ) # 왼쪽 공백제거
print('[%s]'%a.rstrip() ) # 오른쪽 공백제거
print('[%s]'%a.strip() )  # 양쪽 공백제거
# 가운데 공백 제거 -> 정규식
# 대소문자
a = 'abcdABCD가나다라1234!@#$'
print( a.upper() )
print( a.lower() )
# 조합사용 
ur1 = 'https://taegon.kim/wp-content/uploads/2018/05/image-5.png'
#  => image-5.png 라는 문자열을 획득하시오, 리스트 인덱싱 정도 사용
# 단, 상수값을 쓰지 않는다.
# 1번 방식
print(ur1.split('/') ) # '/'제거 (분해)
print(ur1.split('/')[-1] )

# 2번 방식
tmp = ur1.split('/')
print(tmp)
print( len(tmp) )
print( ur1.count('/') )
print( tmp[-1] )                         # tmp 의 끝에서 첫번재
print( tmp[len(tmp)-1] )                 # tmp길이 -1 은 7번쨰
print( ur1.split('/')[ur1.count('/')])   # 분해 후 7번째 인덱스

# 3. 내가 한거
b = list(ur1)              # url을 하나씩 다 쪼갠다
print(b)
print(b[-11:-4])
print(''.join(b[-11:-4]) ) # 조인을 통해 범위를 설정하고 합침

#포멧팅
a = 1
b = 2
# x+y = z 형식으로 출력
print( '%d + %d = %d' %(a,b,a+b) )
# %s로 받는 경우 => 데이터가 문자열일때, 데이터의 타입을 모를 때 
print( '%s + %s = %s' %(a,b,a+b) )
print( '%d / %d = %f' %(a,b,a+b) )
print( '%d + %d = %s' %(a,b,a+b) )
# .format() 처리
print( '{}+{} = {}' .format(a,b,a+b)) # format을 사용하면'자리에 순서대로 들어 간다.'는 의미
print( '{0} + {1} = {2}' .format(a,b,a+b) )
print( '{1} + {0} = {2}' .format(a,b,a+b) )
# format의 파라티터를 모두 다 쓸 필요는 없는 것을 보여준다. 
print( '{1} + {1} = {1}' .format(a,b,a+b) )
print( '{1} + {0} = {result}' .format(a,b,result=a+b))
# erorr
# print( result ) # result 자체는 지역변수.
# 포멧팅, 자리수 체크
print( '[%s]' %'12345')
# 20칸에 배치
print( '[%20s]' %'12345')  # 뒤쪽으로 정렬
print( '[%-20s]' %'12345') # 앞쪽으로 정렬
print( '[%0.2f]' %12345.12345) # 소수점 자리 체크
print( '[%0.2f]' %12345.12665) # 소수점 자리를 체크하되 반올림인지 확인
# 전체데이터가 10칸
print( '[%10.2f]' %123.456)
# 뒤쪽 정렬
print( '[%10s]' %'12345')
# 치환식 
a = 'abc{}defg' .format('k')
print(a)
# 자리수 10개, 앞쪽 위치
a = 'abc{0:<10}defg' .format('k')
print(a)
# 10칸 중 뒤쪽
a = 'abc{0:>10}defg' .format('k')
print(a)
# 짝수칸일 경우 앞쪽으로 센터 위치
a = 'abc{0:^10}defg' .format('k')
print(a)
# *로 빈칸 채우기
a = 'abc{0:*^10}defg' .format('k')
print(a)