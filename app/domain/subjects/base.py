from abc import ABC, abstractmethod

from app.domain.ticket.models import Ticket


class BaseSubject(ABC):
    """
    Classe base para todos os assuntos do sistema.
    """

    name: str
    description: str

    @abstractmethod
    def execute(self, ticket: Ticket) -> str:
        """
        Executa a regra do assunto e retorna a resposta.
        """
