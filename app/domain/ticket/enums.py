from enum import Enum


class TicketStatus(str, Enum):
    """
    Possíveis estados de um atendimento.
    """

    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"
