from app.domain.ticket.models import Ticket
from app.domain.ticket.repository import TicketRepository
from app.domain.ticket.service import TicketService


class CloseTicketService:
    """
    Caso de uso responsável por fechar um Ticket.
    """

    def __init__(
        self,
        repository: TicketRepository,
    ) -> None:
        self.ticket_service = TicketService(repository)

    def execute(
        self,
        ticket_id: str,
    ) -> Ticket:
        return self.ticket_service.close(ticket_id)
