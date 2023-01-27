# # coding: utf-8
# from sqlalchemy import Column, ForeignKey, String
# from sqlalchemy.dialects.mysql import INTEGER
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# metadata = Base.metadata


# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(255))
#     username = Column(String(255))
#     email = Column(String(255), primary_key=True, index=True)
#     password = Column(String(255))


# class Blog(Base):
#     __tablename__ = 'blogs'

#     blog_id = Column(INTEGER(11), primary_key=True, index=True)
#     title = Column(String(255))
#     body = Column(String(255))
#     user = Column(ForeignKey('user.email'), index=True)

#     user1 = relationship('User')
