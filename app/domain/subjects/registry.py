from app.domain.subjects.base import BaseSubject
from app.domain.subjects.cliente_atraso.subject import ClienteEmAtrasoSubject


class SubjectRegistry:
    """
    Registro responsável por armazenar
    todos os assuntos disponíveis.
    """

    def __init__(self):
        self._subjects: dict[str, BaseSubject] = {}

    def register(self, subject: BaseSubject):
        key = subject.name.lower()

        if key in self._subjects:
            raise ValueError(f"Subject '{subject.name}' já registrado.")

        self._subjects[key] = subject

    def get(self, name: str) -> BaseSubject:
        key = name.lower()

        if key not in self._subjects:
            raise KeyError(f"Subject '{name}' não encontrado.")

        return self._subjects[key]

    def list(self) -> list[BaseSubject]:
        return list(self._subjects.values())


# -----------------------------------------------------------------------------
# Registry global da aplicação
# -----------------------------------------------------------------------------

registry = SubjectRegistry()

registry.register(ClienteEmAtrasoSubject())
