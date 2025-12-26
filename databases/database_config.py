from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.schema import CreateTable

DATABASE_URL = "sqlite:///databases/users.db"


# Создаём Engine
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ ="users"

    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str|None] = mapped_column()
    lang: Mapped[str|None] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)

Base.metadata.create_all(engine)

print(CreateTable(Users.__table__))