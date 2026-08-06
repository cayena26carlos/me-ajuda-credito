from dataclasses import dataclass


@dataclass(slots=True)
class SubjectResult:
    """
    Resultado da execução de um Subject.

    Futuramente poderá conter:
    - warnings
    - metadata
    - actions
    - external_data
    """

    message: str
    success: bool = True
