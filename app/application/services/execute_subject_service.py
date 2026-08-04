from app.api.schemas.subjects import (
    ExecuteSubjectRequest,
    ExecuteSubjectResponse,
)
from app.application.services.subject_execution_service import (
    SubjectExecutionService,
)
from app.domain.ticket.service import TicketService


class ExecuteSubjectService:
    """
    Orquestra a abertura de um Ticket e a execução
    do fluxo correspondente ao tipo de atendimento.
    """

    def __init__(self):
        self.ticket_service = TicketService()
        self.subject_execution_service = SubjectExecutionService()

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

        message = self.subject_execution_service.execute(ticket)

        return ExecuteSubjectResponse(
            ticket_id=ticket.id,
            status=ticket.status.value,
            message=message,
        )
