from sqlalchemy import  String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid
import enum

from ..core.database import Base

class OTPPurpose(enum.Enum):
    LOGIN = "login"
    REGISTER = "register"
    RESET_PASSWORD = "reset_password"


class OTP(Base):
    __tablename__ = "otp"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))

    target: Mapped[str] = mapped_column(String(50))  # email or phone
    code: Mapped[str] = mapped_column(String)  # hashed
    purpose: Mapped[OTPPurpose] = mapped_column(Enum(OTPPurpose))

    consumed: Mapped[bool] = mapped_column(Boolean, default=False)
    attempts: Mapped[int] = mapped_column(default=0)
    sent_via: Mapped[str] = mapped_column(String(20))  # sms or email

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime)

    user = relationship("User", back_populates="otps")
