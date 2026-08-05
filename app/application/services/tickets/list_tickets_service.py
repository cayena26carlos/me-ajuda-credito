from app.domain.ticket.models import Ticket
from app.domain.ticket.service import TicketService


class ListTicketsService:
    """
    Caso de uso responsável por listar os Tickets.
    """

    def __init__(self):
        self.ticket_service = TicketService()

    def execute(self) -> list[Ticket]:
        return self.ticket_service.list()
