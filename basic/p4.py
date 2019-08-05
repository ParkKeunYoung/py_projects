'''
       > 딕셔너리 : {} -> , 
                         js의 객체와 동일, 순서 x, 키: 값, 키는 중복되면 안됨,
                         값 중복은 허용
                    => 테이블상의 한 개의 row,json의 객체
'''

# 이 스타일을 가장 많이 사용
dic = {}
print(dic, len(dic), type(dic))
dic = dict()
print(dic, len(dic), type(dic))
#####################################################################################
# 키를 통해서 값을 이해할 수 있다. 직관적으로
dic = {
    'name' : '홍길동',
    'age'  : 100
}
print(dic, len(dic), type(dic))
# 인덱싱 : 딕셔너리는 순서가 없으므로, 데이터를 특정할 수 있는 키 값을 사용한다.
print(dic['name'])
# 데이터추가, 키는 모든지 올 수 있다. 2는 인덱스가 아닌 => <<< 키를 의미!! >>>
dic[2] = 'hello'
print(dic, len(dic), type(dic))
print( dic[2] )
#####################################################################################
print( dic.keys() ) # 키 list 출력
print( dic.values() )
# 키 조사 
print( 'name' in dic )
# for문으로 돌려보기 => for 에서 확인
