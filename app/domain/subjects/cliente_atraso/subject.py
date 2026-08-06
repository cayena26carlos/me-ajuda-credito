from app.domain.subjects.base import BaseSubject
from app.domain.subjects.enums import SubjectType
from app.domain.subjects.result import SubjectResult
from app.domain.ticket.models import Ticket

from .service import ClienteEmAtrasoService


class ClienteEmAtrasoSubject(BaseSubject):
    """
    Subject responsável pelo fluxo Cliente em atraso.
    """

    name = SubjectType.CLIENTE_EM_ATRASO
    description = "Cliente possui pendências financeiras."

    def __init__(self):
        self.service = ClienteEmAtrasoService()

    def execute(
        self,
        ticket: Ticket,
    ) -> SubjectResult:
        """
        Executa o fluxo do Subject Cliente em atraso.
        """
        return self.service.execute(ticket)
