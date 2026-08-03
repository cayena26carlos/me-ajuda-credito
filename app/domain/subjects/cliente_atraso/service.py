from app.domain.ticket.models import Ticket

from .template import CLIENTE_EM_ATRASO_TEMPLATE


class ClienteEmAtrasoService:
    """
    Regras de negócio do assunto Cliente em atraso.
    """

    def execute(self, ticket: Ticket) -> str:
        return CLIENTE_EM_ATRASO_TEMPLATE
