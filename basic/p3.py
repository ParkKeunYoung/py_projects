'''
    - 연속데이터(시퀸스 타입)
      > 리스트   : [] -> js의 배열과 동일, 순서가 존재, 값 중복 ok, 
                   인덱스는 정방향/역방향(-1,-2, ... ) 존재
'''

# 비워있는 리스트 생성
nums = []     # 정적생성 : 일반적으로 문제는 없으나, 간혹 추가가 안되는 경우가 생김, 이런 경우 동적 생성으로 대체
              #              => 자료구조를 직접 맞춰서 데이터를 세팅하는 리스트 내포같은 케이스에 사용
print( nums, len(nums),type(nums) )
nums = list() # 동적생성 => 대량의 작업 시 조금 더 안정적
print( nums, len(nums),type(nums) ) 
nums = [1,3,5,7,9]
print( nums, len(nums),type(nums) ) 
anis = ['dog','cat','bird']
print( anis, len(anis), type(anis) )
# 리스트에 맴버들의 타입이 다르면 리스트를 구성할 수 없다?
mix = [1,2,3,'cat','dog']
print(mix, len(mix), type(mix))
#   => 파이썬의 모든 것이 객체이므로, 맴버들도 모두 객체 => 주소를 가지고 있음, 이것이 포함
# 차원을 섞으면> 맴버 중에 하나가 리스트였다. 
multiTypeMatrix = [1,2,3,'cat','dog',['brid',100]]
print(multiTypeMatrix, len(multiTypeMatrix), type(multiTypeMatrix))
##################################################################################################
# multiTypeMatrix 에서 100 이란 값을 출력하시오.
# 인덱싱
print(multiTypeMatrix[-1][1])
##################################################################################################
# 슬라이싱 => 사본작업
nums = [1,3,5,7,9]
# nums 에서 3,5,7만 가진 리스트를 구하시오. : 리스트 -> 리스트(슬라이싱: 차원유지)
print( nums[1:-1], '사본출력' )
# 원본은 유지된다 => 원본변경 방법은
nums[0] = 100   # => 인덱싱을 활용한 변경
print( nums )
# 3,5,7 을 모두 -1로 변경하시오.
nums[1:-1] = '-1' # 같은 시퀀스( 연속 데이터 ) 타입이면 슬라이싱 범위를 대체 할 수 있다. 
                  #  => 즉 '-1'은 되지만 -1 은 안된다.
##################################################################################################
# 맴버삭제
del nums[0]
print(nums)
# 9값을 가진 맴버를 제거
nums.remove(9)
print(nums)
nums = [1,3,3,3,5,7]
# 중복된 데이터중 가장 먼저(정방향) 찾은 맴버를 제거
nums.remove(3)
print(nums)
# 다 제거
nums.clear()
print( nums )
# 맴버 추가
nums.append(1)
print(nums)
tmp = [3,5]
# append, extend 는 둘 다 추가를 하지만
# append는 자식을 추가
# extend는 리스트를 이어 붙임 ( 같은 급으로 취급함 ) => 원본 변경
nums.append(tmp)
print(nums)
nums.extend(tmp)
print(nums)
# 두 개를 이어 붙여서 리턴 => 사본작업
print( nums + tmp )  # extend와 같이 이어붙임. 차이점은 extend는 원본변경, 이 방식은 사본작업
print( nums )
# 리스트와 for => for 문에서 확인
