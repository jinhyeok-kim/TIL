# https://wikidocs.net/89

class Book:
  
  def setData(self, title, price, author):
    self.title = title
    self.price = price
    self.author = author

  # def printData(self):
  #   print('제목 : ', self.title)
  #   print('가격 : ', self.price)
  #   print('저자 : ', self.author)
  

  # 프린팅
  # return 문을 사용하는것만 눈여겨보면 됨
  # __repr__은 '문자열'을 'return'한다고 생각하면 됨
  def __repr__(self):
    return self.title

  # __init__ : 어떤 클래스 객체가 만들어질 때, 자동으로 호출 되어 객체가 갖게 될 여러가지 성질을 정해줌
  # 생성자 역할이랑 비슷한거 같기도?(같은건가)
  def __init__(self):
    # self.setData(title, price, author)
    print('책 객체 생성')