from app.domain.subjects.result import SubjectResult
from app.domain.ticket.models import Ticket

from .template import CLIENTE_EM_ATRASO_TEMPLATE


class ClienteEmAtrasoService:
    """
    Regras de negócio do assunto Cliente em atraso.
    """

    def execute(
        self,
        ticket: Ticket,
    ) -> SubjectResult:
        """
        Executa a regra de negócio do Subject.
        """
        return SubjectResult(
            message=CLIENTE_EM_ATRASO_TEMPLATE,
        )
