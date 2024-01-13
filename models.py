from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey('role_table.id'))


class Role(Base):
    __tablename__ = 'role_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

