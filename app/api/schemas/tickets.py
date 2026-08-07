from datetime import datetime

from pydantic import BaseModel

from app.domain.subjects.enums import SubjectType
from app.domain.ticket.enums import TicketStatus


class TicketResponse(BaseModel):
    """
    Representação pública de um Ticket.
    """

    ticket_id: str
    cnpj: str
    subject: SubjectType
    status: TicketStatus
    created_at: datetime
    resolved_at: datetime | None = None


class TicketListResponse(BaseModel):
    """
    Resposta da listagem de Tickets.
    """

    tickets: list[TicketResponse]
