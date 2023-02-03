from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()


class Person(Base):

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    def __repr__(self):

        return f"<Person({self.first_name} {self.last_name})>"

    def greeting(self):

        print(f'{self.first_name} says "hello"!')
