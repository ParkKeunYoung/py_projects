# 함수
# function, method
# 반복작업 해소, 재활용성 높이고, 구조적 설계 => 개발시간 단축
'''
def 함수명( [인자명, 인자명, ... ] ):
        statement # 수행문
        [ return 값]
'''
# 함수 정의
def add(x, y):
        return x+y
# 함수 사용
d = add(1,2)
print(d)

# 가변인자, 함수의 입력의 수가 가변
def add2( *args ):
        print( args )
        # 인자로 전달된 데이터를 모두 더해서 (누적 합) 리턴하시오
        sum = 0
        for arg in args:
                sum += arg
        return sum

print ( add2(1,2) )
print ( add2(1,2,3) )

# 가변 인자로 전달 된 누적 합과 누적 곱을 리턴하시오
def mix( *args ):
        print( args )
        sum, mul = (0, 1)
        for arg in args:
                sum += arg
                mul *= arg
        # 리턴 할 값이 여러개면 튜플로 리턴된다.
        return sum,mul

print ( mix(1,2) )
print ( mix(1,2,3,4) ) # 튜플로 나타내어짐
# 데이터를 받을 때 반드시 순서를 확인해야한다. --> 순서가 싫다면 딕셔너리를 사용
a,b = mix(1,2,3,4) # 각각 값을 넣어줌
print(a)
print(b)

# 리턴을 딕셔너리로 해보자 -> 출력 결과에 대해서 순서를 몰라도 된다. 키만 알면 된다.
def mix2( *args ):
        print( args )
        sum, mul = (0, 1)
        for arg in args:
                sum += arg
                mul *= arg
        return { "sum":sum, 'mul':mul }
print(mix2(1,2,3,4,5)['mul'],mix2(1,2,3)['sum'])

# 로그함수
env_debug = True
def log( msg ):
        if env_debug:        
                print('-'*40)
                print( msg )
                print('-'*40)
log('이 것은 로그 메시지 출력 함수이다')

# 사용자 정의 함수 : 형태를 정의 할 수 없다. 만드는 사람 마음이기 떄문에 ==> 프로젝트시 네이밍에 대한 정의가 필요하다.
# pk_ml_analysis_xxx
# 내장함수 : 1en(), type(), int(), str(), tuple(), dict(), list()
# 외장함수 : random.randint(), sys.exit()


# 함수 인자의 초기값주기 
# 초기값이자들이 존재하면, 초기값 인자는 앞으로 와야한다.
# def setPerson(  name='품질', age=20, weight=60, score ):
def setPerson(  score, name='품질', age=20, weight=60 ):
        log( '%s %s %s %s' %(name,age,weight,score) )

setPerson(100)
setPerson(score = 50)
# 기본 값이 없는 함수의 파라미터는 반드시 값을 부여해야 한다. 그렇지않을 경우 오류.
# erorr
# setPerson(name ='모라') # score가 빠짐
setPerson(1,2,3,4)
# 기본값이 부여된 파라미터들은 함수 호출시 순서에 상관없이 명시적으로 사용가능
setPerson(1, age = 100, name = '모라' )

log( msg = '가나다라' )
log('가나다라')