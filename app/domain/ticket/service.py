from datetime import UTC, datetime

from app.domain.subjects.enums import SubjectType
from app.domain.ticket.enums import TicketStatus
from app.domain.ticket.exceptions import TicketNotFound
from app.domain.ticket.models import Ticket
from app.domain.ticket.repository import TicketRepository


class TicketService:
    """
    Serviço responsável por manipular Tickets.
    """

    def __init__(
        self,
        repository: TicketRepository,
    ) -> None:
        self._repository = repository

    def create(
        self,
        cnpj: str,
        subject: SubjectType,
        user_id: str,
        channel: str,
        thread_ts: str,
        details: str | None = None,
    ) -> Ticket:
        ticket = Ticket(
            cnpj=cnpj,
            subject=subject,
            user_id=user_id,
            channel=channel,
            thread_ts=thread_ts,
            details=details,
        )

        return self._repository.save(ticket)

    def find(self, ticket_id: str) -> Ticket:
        ticket = self._repository.find_by_id(ticket_id)

        if ticket is None:
            raise TicketNotFound(f"Ticket '{ticket_id}' não encontrado.")

        return ticket

    def close(self, ticket_id: str) -> Ticket:
        ticket = self.find(ticket_id)

        if ticket.status != TicketStatus.CLOSED:
            ticket.status = TicketStatus.CLOSED
            ticket.resolved_at = datetime.now(UTC)

        return self._repository.save(ticket)

    def list(self) -> list[Ticket]:
        return self._repository.list_all()
