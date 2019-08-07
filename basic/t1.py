# 여기는 game에서 사용할 거 test 함

# 문자열을 숫자(정수)로 변환이 가능한지 체크하는 내용
A = [''
,'1'
,'1.1'
,'A'
,'a'
,'@'
,'가'
]

for data in A:
    print( data, data.isalpha(), data.isnumeric(), data.isdecimal(), data.isdigit() )

# 외장함수 => 사용할때는 가져오는 절차 import가 반드시 같이 존재한다!
  # 모듈을 가져와서 그 안에 존재하는 함수를 사용하는 케이스
import random
for n in range(10):
    # 시작경계값 <= 난수 <= 끝경계값
    print( random.randint(0,99) )