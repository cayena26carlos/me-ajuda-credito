from app.api.schemas.subjects import (
    ExecuteSubjectRequest,
    ExecuteSubjectResponse,
)
from app.application.services.subjects.subject_engine import SubjectEngine
from app.domain.ticket.repository import TicketRepository
from app.domain.ticket.service import TicketService


class ExecuteSubjectService:
    """
    Orquestra a abertura de um Ticket e a execução
    do fluxo correspondente ao tipo de atendimento.
    """

    def __init__(
        self,
        repository: TicketRepository,
    ) -> None:
        self.ticket_service = TicketService(repository)
        self.subject_engine = SubjectEngine()

    def execute(
        self,
        request: ExecuteSubjectRequest,
    ) -> ExecuteSubjectResponse:
        ticket = self.ticket_service.create(
            cnpj=request.cnpj,
            subject=request.subject,
            user_id=request.user_id,
            channel=request.channel,
            thread_ts=request.thread_ts,
            details=request.details,
        )

        result = self.subject_engine.execute(ticket)

        return ExecuteSubjectResponse(
            ticket_id=ticket.id,
            status=ticket.status.value,
            message=result.message,
        )
