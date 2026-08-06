from abc import ABC, abstractmethod

from app.domain.subjects.result import SubjectResult
from app.domain.ticket.models import Ticket


class BaseSubject(ABC):
    """
    Classe base para todos os Subjects do sistema.
    """

    name: str
    description: str

    @abstractmethod
    def execute(
        self,
        ticket: Ticket,
    ) -> SubjectResult:
        """
        Executa o Subject e retorna o resultado da execução.
        """
        ...
