from pydantic import BaseModel


class ExecuteSubjectRequest(BaseModel):
    """
    Payload para execução de um Subject.
    """

    subject: str
    user_id: str
    channel: str
    thread_ts: str
