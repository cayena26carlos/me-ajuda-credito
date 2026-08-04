from pydantic import BaseModel

from app.domain.subjects.enums import SubjectType


class ExecuteSubjectRequest(BaseModel):
    """
    Payload para abertura e execução de um atendimento.
    """

    cnpj: str
    subject: SubjectType
    details: str | None = None

    user_id: str
    channel: str
    thread_ts: str


class ExecuteSubjectResponse(BaseModel):
    """
    Resposta da execução do Subject.
    """

    ticket_id: str
    status: str
    message: str
