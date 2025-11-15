from sqlalchemy import  String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid

from ..core.database import Base

class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))

    token: Mapped[str] = mapped_column(String)  # hashed token
    jti: Mapped[str] = mapped_column(String, unique=True)

    issued_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime)
    revoked: Mapped[bool] = mapped_column(Boolean, default=False)

    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    device_info: Mapped[str | None] = mapped_column(Text, nullable=True)

    user = relationship("User", back_populates="refresh_tokens")
