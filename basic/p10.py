# 반복문 => for문

a = [1,2,3,4,5]
b = {
    'name' : '품질',
    'addr' : '모라'
}
c = (1,3,5,7,9)

#for ~ each 스타일만 지원
for item in a:
    # 리스트를 for문으로 돌리면 맴버를 하나씩 꺼낸다.
    print(item)

for item in c:
    # 튜플도 리스트와 마찬가지
    print(item)

for item in b:
    # 딕셔너리는 키 값만 불러온다
    print(item)
for key in b:
    # 키 + 값을 불러온다.
    print(key, b[key])

d = [(1,2),(3,4),(5,6)]
# 튜플은 변수로 받을 때 맴버수와 동수로 변수를 나열하면 순서대로 들어간다.
for i,j in d:
    print(i,j)

# 딕셔너리에서 만약 인덱스를 뽑고 싶다면
for idx,key in enumerate(b): # enumerate = 내장함수 
    print(idx,key)

# 연속수 만드는 내장함수 => range()
# 0 부터 n <3: 경계값 (3(경계값) 앞까지 뽑음)
for n in range(3):
    print(n)
# 1: 시작값, 4: 경계값
for n in range(1,4):
    print(n)
# 1: 시작값, 11: 경계값, 2: step(간격)
for n in range(1,11,2):
    print(n)
########################################################################################
# Mission
# 3~7 단 구구단 구현
# 형식 : 3 x 1 = 3, 곱의 결과의 자리수는 최대 2자리이다, 1자리 값일 떄 좌측정렬로 표현
for i in range(3,8):
    for j in range(1,10):
        print('{0} x {1} = {2:>2}' .format(i,j,i*j)) 

# 만약 결과를 리스트로 담고 싶다면.
result = list()
for i in range(3,8):
    for j in range(1,10):
        # 리스트에 생성된 문자열을 맴버로 추가
        result.append('{0} x {1} = {2:>2}' .format(i,j,i*j)) 
print(result)

# 코드를 한줄로 줄이면 => 리스트 내포 ,딕셔너리 내포, 시퀸스 타입은 다 가능하다.
# 작성법 => 결론의 형태부터 완성 => 각 변수를 기술하면 된다 => 조건이 있으면 추가
result1 = [ '{0} x {1} = {2:>2}' .format(i,j,i*j) 
            for i in range(3,8) 
            for j in range(1,10) ]
print(result1)
########################################################################################