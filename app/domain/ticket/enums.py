from enum import StrEnum


class TicketStatus(StrEnum):
    """
    Possíveis estados de um atendimento.
    """

    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"
