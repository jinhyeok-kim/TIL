# 참고 : https://niceman.tistory.com/181
from abc import ABC, abstractmethod

# 팩토리 메소드 패턴(Factory Method Pattern)
# 객체를 생성하기 위한 인터페이스를 정의하고, 인스턴스 생성은 서브 클래스가 결정하게 된다.

# - 객체 생성을 캡슐화하는 패턴

class DBManager(ABC):
  @abstractmethod # 추상 메소드 선언
  def connection(self):
    pass

class SqlServer(DBManager):
  def connection(self):
    return ('MicroSoft Database Connected.')

class Oracle(DBManager):
  def connection(self):
    return ('Oracle Database Connected.')

class MariaDB(DBManager):
  def connection(self):
    return ('Maria Database Connected.')

class DBConnFactory:
  def get_db_connection(self, db):
    return db.connection()

db_fact = DBConnFactory() # DbConnFactory 클래스 인스턴스 생성

# 각 DB 가상 연결 테스트 출력
print(db_fact.get_db_connection(SqlServer()))
print(db_fact.get_db_connection(Oracle()))
print(db_fact.get_db_connection(MariaDB()))