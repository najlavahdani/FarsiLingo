from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid

from ..core.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[str] = mapped_column(String)  # hashed
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=True)
    profile_picture: Mapped[str | None] = mapped_column(String, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_email_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    roles = relationship("UserRole", back_populates="user")
    otps = relationship("OTP", back_populates="user")
    refresh_tokens = relationship("RefreshToken", back_populates="user")
    sessions = relationship("AuthSession", back_populates="user")
    password_resets = relationship("PasswordReset", back_populates="user")
