from app.domain.subjects.base import BaseSubject
from app.domain.ticket.models import Ticket

from .template import CLIENTE_EM_ATRASO_TEMPLATE


class ClienteEmAtrasoSubject(BaseSubject):
    name = "cliente_em_atraso"

    description = "Cliente possui pendências financeiras."

    def execute(self, ticket: Ticket) -> str:
        return CLIENTE_EM_ATRASO_TEMPLATE
