from pydantic import BaseModel


class ExecuteSubjectResponse(BaseModel):
    """
    Resposta da execução do Subject.
    """

    ticket_id: str
    status: str
    message: str
