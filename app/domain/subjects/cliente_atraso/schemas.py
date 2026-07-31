from pydantic import BaseModel


class ClienteEmAtrasoResponse(BaseModel):
    message: str
