from sqlalchemy import String, DateTime, Text 
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid

from ..core.database import Base

class Role(Base):
    __tablename__ = "role"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    users = relationship("UserRole", back_populates="role")
