# class
# 파이썬에서 자기 자신 객체를 가르키는 키워드 self
# self => phthon, objective-c
# this => java, is, 대다수 랭귀지
class Person:
    '''
    맴버 변수
    '''
    name   = None
    age    = 0
    weight = 0

    '''
    맴버 함수
    '''
    def eat(self,food):
        print('%s를 먹는다' %food)
    '''
    생성자 : 객체를 생성하고 맴버 변수를 초기화 하는게 목적
    '''
    def __init__(self, name, age, weight):
        # 클래스 내부에서 맴버들을 접근할 떄, self.맴버(변수/함수)
        self.name = name
        self.age = age
        self.weight = weight
        # 부모 생성자 호출
        # return super().__init__()
    '''
    객체를 설명하는 코드를 구현된다. 통상 문자열로 구성 
    맴버 변수값이나 상태를 표현한 정보가 들어오면 ok
    자바의 toString()의 맥락과 유사
    '''
    def __repr__(self):
        return '''
            name=%s, age=%s, weight =%s
            ''' %(self.name,self.age,self.weight)

# 객체 생성
obj = Person('품질',1,2) 
print(obj)
obj.eat('사과')