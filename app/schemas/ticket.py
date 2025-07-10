from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Ticket(BaseModel):
    id: str
    title: str
    status: str
    priority: Optional[str] = None
    created_at: datetime
    updated_at: datetime