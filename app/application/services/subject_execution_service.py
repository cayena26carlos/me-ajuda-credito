from app.domain.subjects.registry import registry
from app.domain.ticket.models import Ticket


class SubjectExecutionService:
    """
    Responsável por executar um Subject
    a partir de um Ticket.
    """

    def execute(self, ticket: Ticket) -> str:
        subject = registry.get(ticket.subject)

        return subject.execute(ticket)
