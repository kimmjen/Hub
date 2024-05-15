from __future__ import annotations

from sqlmodel import Field, Relationship, SQLModel


# Generic message
class Message(SQLModel):
    message: str
