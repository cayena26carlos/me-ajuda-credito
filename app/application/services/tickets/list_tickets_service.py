from app.domain.ticket.models import Ticket
from app.domain.ticket.repository import TicketRepository
from app.domain.ticket.service import TicketService


class ListTicketsService:
    """
    Caso de uso responsável por listar todos os Tickets.
    """

    def __init__(
        self,
        repository: TicketRepository,
    ) -> None:
        self.ticket_service = TicketService(repository)

    def execute(self) -> list[Ticket]:
        return self.ticket_service.list()
