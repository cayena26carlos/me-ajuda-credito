from app.domain.subjects.base import BaseSubject
from app.domain.ticket.models import Ticket

from .service import ClienteEmAtrasoService


class ClienteEmAtrasoSubject(BaseSubject):
    """
    Subject responsável pelo fluxo Cliente em atraso.
    """

    name = "cliente_em_atraso"

    description = "Cliente possui pendências financeiras."

    def __init__(self):
        self.service = ClienteEmAtrasoService()

    def execute(self, ticket: Ticket) -> str:
        return self.service.execute(ticket)
