from configs import settings

from sqlalchemy import create_engine, Column, String, Integer, TIMESTAMP, ForeignKey, func
from sqlalchemy import orm, schema

import uuid


engine = create_engine(settings.DB_URI)
SessionLocal = orm.sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = orm.declarative_base()


class User(Base):
    __tablename__ = "users"

    userID = Column(String(150), primary_key=True)
    platformName = Column(String(150), nullable=False)
    platformUserID = Column(String(150), nullable=False)
    createdAt = Column(TIMESTAMP, server_default=func.now())
    lastSeenAt = Column(TIMESTAMP, onupdate=func.now(), server_default=func.now())

class CourseCompletion(Base):
    __tablename__ = "courses_ep_complete"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(String(150))
    courseSlug = Column(String(150))
    epSlug = Column(String(150))
    createdAt = Column(TIMESTAMP, server_default=func.now())


def create_tables():
    Base.metadata.create_all(bind=engine)


def create_new_user(db:orm.Session, platform_name:str, platform_user_id:str):
    user_id = uuid.uuid4()
    user = User(userID=user_id, platformName=platform_name, platformUserID=platform_user_id)
    db.add(user)
    db.commit()
    db.refresh()
    return user


def get_user_by_platform(db:orm.Session, platform_name:str, platform_user_id:str):
    return (db.query(User)
              .filter(User.platformName==platform_name)
              .filter(User.platformUserID==platform_user_id)
              .first())


def get_or_create_user(db:orm.Session, platform_name:str, platform_user_id:str):
    user = get_user_by_platform(db, platform_name=platform_name, platform_user_id=platform_user_id)
    if user == None:
        return create_new_user(db, platform_name=platform_name, platform_user_id=platform_user_id)
    return user


def get_courses_complet_by_user(db:orm.Session, user_id:str):
    return db.query(CourseCompletion).filter(User.userID==user_id).all()


def insert_user_course_ep(db:orm.Session, user_id:str, course_slug:str, ep_slug:str):
    completion = CourseCompletion(userID=user_id, courseSlug=course_slug, epSlug=ep_slug)
    db.add(completion)
    db.commit()


def delete_user_course_ep(db:orm.Session, user_id:str, course_slug:str, ep_slug:str):
    completion = (db.query(CourseCompletion)
                   .filter_by(
                        userID=user_id,
                        courseSlug=course_slug,
                        epSlug=ep_slug)
                    .first())
    if completion:
        db.delete(completion)
        db.commit()
