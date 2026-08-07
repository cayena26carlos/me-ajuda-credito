from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from app.domain.subjects.enums import SubjectType
from app.domain.ticket.enums import TicketStatus


@dataclass
class Ticket:
    """
    Representa um atendimento aberto pelo usuário.
    """

    cnpj: str
    subject: SubjectType
    user_id: str
    channel: str
    thread_ts: str
    details: str | None = None

    id: str = field(default_factory=lambda: str(uuid4()))
    status: TicketStatus = TicketStatus.OPEN
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    resolved_at: datetime | None = None
