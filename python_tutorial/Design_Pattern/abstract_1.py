from abc import ABCMeta, abstractmethod
# abc : abstract base class의 약자
# 클래스의 ()안에 metaclass=ABCMeta를 지정하고, @abstractmethod 붙여서 추상 메소드로 지정

# @abstarctmethod로 지정해주면, Animal을 상속 받는 클래스는
# 무조건 say 메소드를 구현 하여야만 객체 생성이 가능
class Animal(metaclass=ABCMeta):
  @abstractmethod
  def say(self):
    pass

class Dog(Animal):
  def say(self):
    print('왈왈!!')

class Cat(Animal):
  def say(self):
    print('냐옹!!')

# 심플 팩토리 패턴 ... 조금 더 공부ㅎ자ㅏ
class ForestFactory(object):
  def make_sound(self, obj_type):
    return eval(obj_type)().say()



if __name__ == '__main__':
  dog = Dog()
  cat = Cat()
  dog.say()
  cat.say()