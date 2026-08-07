from typing import Protocol

from app.domain.ticket.models import Ticket


class TicketRepository(Protocol):
    """
    Contrato de persistência para Tickets.
    """

    def save(self, ticket: Ticket) -> Ticket: ...

    def find_by_id(self, ticket_id: str) -> Ticket | None: ...

    def list_all(self) -> list[Ticket]: ...
