from app.domain.subjects.registry import registry
from app.domain.subjects.result import SubjectResult
from app.domain.ticket.models import Ticket


class SubjectEngine:
    """
    Responsável por localizar e executar o Subject correspondente ao Ticket.
    """

    def execute(
        self,
        ticket: Ticket,
    ) -> SubjectResult:
        subject = registry.get(ticket.subject.value)

        return subject.execute(ticket)
