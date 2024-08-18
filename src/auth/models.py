from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.db import Base


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # avatar: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(default=True)
    avatar: Mapped[str] = mapped_column(String, nullable=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=True)
    role: Mapped["Role"] = relationship("Role", lazy="selectin")
    contacts: Mapped[list["Contact"]] = relationship("Contact", back_populates="owner")
