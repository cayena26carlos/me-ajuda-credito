from app.domain.ticket.models import Ticket
from app.domain.ticket.service import TicketService


class CloseTicketService:
    """
    Caso de uso responsável por fechar um Ticket.
    """

    def __init__(self) -> None:
        self.ticket_service = TicketService()

    def execute(
        self,
        ticket_id: str,
    ) -> Ticket:
        return self.ticket_service.close(ticket_id)
