from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import uuid

from ..core.database import Base

class UserRole(Base):
    __tablename__ = "user_role"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("role.id"), primary_key=True)

    assigned_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")
