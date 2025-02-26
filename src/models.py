from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from eralchemy2 import render_er

Base = declarative_base()

class Profile (Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    #relacion con Story de 1 a muchos
    stories = relationship("Story", back_populates="profile")
    #relacion con Post de 1 a muchos
    posts = relationship("Post", back_populates="profile")

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    views = Column(Integer)
    comments = Column(Integer)
    tags = Column(String)
    music = Column(String)
    likes = Column(Integer, default=0)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    #relacion inversa con Profile
    profile = relationship("Profile", back_populates="stories")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    comments = Column(Integer)
    tags = Column(String)
    music = Column(String)
    likes = Column(Integer, default=0)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    #relacion inversa con Profile
    profile = relationship("Profile", back_populates="posts")

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    messages = Column(String)
    sender_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)

try:
    render_er(Base, "diagram.png")
    print("Diagrama UML generado con éxito como 'diagram.png'")
except Exception as e:
    print(f"Error al generar diagrama: {e}")