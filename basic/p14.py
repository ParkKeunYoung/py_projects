######################################################################################################
# 모듈화 + 패키지
# 모듈 만들기, 테스트 코드 배치, 모듈 가져오기, 패키지 사용
# basic -> a 폴더 만듬
# 모듈 => *.py
#          mod.py, __init__.py, p1.py, p2.py, ...
# 모듈화의 대상 => 변수, 함수, 클래스 <= 이런 요소를 가져다 내것처럼 사용가능
#                 ex) 앞서 만든 PI, PI2, PI3, add
# 패키지 => 유사한기능끼리 묶어둔 디렉토리, 유틸리티, 통신, gui 등등 모아둔것
#           ex) 앞서 만든  a, b 폴더
#           패키지 폴더 내에 존재하는 __init__.py 이 파일은 하위 호환을 위해서 python3.3 이하 에서는 모두
#           사용한다. 그리고 __init__.py는 곧 해당 패키지 자체를 의미한다.
######################################################################################################
# from 패키지.패키지....모듈 import 변수, 함수, 클래스( 필요한 것들 열거 )
from a.b.mod import PI, add
print(PI)
print(add(1,2))

# from 패키지.패키지 import  변수, 함수, 클래스( 필요한 것들 열거 )
# 경로상 마지막 패키지(디렉토리) 안에 있는 __init__.py에서 모듈을 가져온다.
from a.b import PI2 as pi2
print(pi2)

# 패키지명은 절대로 '.' 들어가면 안된다.
# 모듈명도 마찬가지로 '.' 들어가면 안된다.
from a import PI3
print(PI3)

# 별칭 = 이름이 너무 길어서나, 혹은 이름을 원하는 것으로 변경해서 사용하고 싶으면 
# ===>  '원래이름 as 별칭' 
from a import PI3 as pi
print(pi)

# 가져올 모듈이 너무 많다. 다 가져왔으면 좋겠다.=====> '*'
# 하위 호환을 위해서는 
# __all__ = ['mod']
from a.b import *
print( mod.PI, PI2)

# import 만 사용시
import a.b as bm  
print( bm.PI2 )          # 마치 외장함수 사용하는것처럼 '.' 붙여 사용

import a.b.mod as m
print(m.PI)

# 모듈을 가져온다는 것은 해당 모듈을 실행한다라고 봐도 무방하다. = > 메모리 적재를 해야되서
# 내가 만든 모듈같은 경우 의도하지 않은 코드가 실행될 수 있다.
# => 테스트 하려고 만든 코드는 모듈 가져오기 수행시 실제로 구동되면 안된다.
# 코드처리가 필요하다. => '__name__'을 이용하여 처리 한다.
# __name__을 사용하는 모듈을 직접 구동하면 '__main__'으로 나오고,
# 모듈로 사용되면(즉, 다른 모듈이 가져다 쓰면) "모듈명"으로 나온다.
from p13_mod import XMan
mu = XMan('데드풀','100','50','51')
print( mu )
print('p14 : __name__', __name__)