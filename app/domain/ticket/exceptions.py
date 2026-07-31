class TicketException(Exception):
    """Exceção base do domínio de Ticket."""


class TicketNotFound(TicketException):
    """Ticket não encontrado."""


class InvalidTicketStatus(TicketException):
    """Status inválido para a operação."""
