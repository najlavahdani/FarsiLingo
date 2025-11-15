from sqlalchemy import  String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid

from ..core.database import Base

class AuthSession(Base):
    __tablename__ = "auth_session"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))

    session_token: Mapped[str] = mapped_column(String)  # hashed
    ip_address: Mapped[str | None] = mapped_column(String(45))
    user_agent: Mapped[str | None] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_active_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    revoked: Mapped[bool] = mapped_column(Boolean, default=False)

    user = relationship("User", back_populates="sessions")
