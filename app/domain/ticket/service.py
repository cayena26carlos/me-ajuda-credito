from app.domain.subjects.enums import SubjectType
from app.domain.ticket.enums import TicketStatus
from app.domain.ticket.exceptions import TicketNotFound
from app.domain.ticket.models import Ticket


class TicketService:
    """
    Serviço responsável por manipular Tickets.
    """

    _tickets: dict[str, Ticket] = {}

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

        self._tickets[ticket.id] = ticket

        return ticket

    def find(self, ticket_id: str) -> Ticket:
        ticket = self._tickets.get(ticket_id)

        if ticket is None:
            raise TicketNotFound(f"Ticket '{ticket_id}' não encontrado.")

        return ticket

    def close(self, ticket_id: str) -> Ticket:
        ticket = self.find(ticket_id)

        ticket.status = TicketStatus.CLOSED

        return ticket

    def list(self) -> list[Ticket]:
        return list(self._tickets.values())
