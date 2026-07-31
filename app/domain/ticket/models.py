from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from app.domain.ticket.enums import TicketStatus


@dataclass
class Ticket:
    """
    Representa um atendimento aberto pelo usuário.
    """

    subject: str
    user_id: str
    channel: str
    thread_ts: str

    id: str = field(default_factory=lambda: str(uuid4()))
    status: TicketStatus = TicketStatus.OPEN
    created_at: datetime = field(default_factory=datetime.utcnow)
