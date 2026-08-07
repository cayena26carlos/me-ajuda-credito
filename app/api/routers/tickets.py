from fastapi import APIRouter, HTTPException, status

from app.api.schemas.tickets import TicketListResponse, TicketResponse
from app.application.services.tickets.close_ticket_service import CloseTicketService
from app.application.services.tickets.get_ticket_service import GetTicketService
from app.application.services.tickets.list_tickets_service import ListTicketsService
from app.domain.ticket.exceptions import TicketNotFound
from app.infrastructure.dependencies import get_ticket_repository

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.get(
    "",
    response_model=TicketListResponse,
    summary="Listar Tickets",
)
def list_tickets() -> TicketListResponse:
    service = ListTicketsService(
        get_ticket_repository(),
    )

    tickets = service.execute()

    return TicketListResponse(
        tickets=[
            TicketResponse(
                ticket_id=ticket.id,
                cnpj=ticket.cnpj,
                subject=ticket.subject,
                status=ticket.status,
                created_at=ticket.created_at,
            )
            for ticket in tickets
        ]
    )


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse,
    summary="Buscar Ticket por ID",
)
def get_ticket(
    ticket_id: str,
) -> TicketResponse:
    service = GetTicketService(
        get_ticket_repository(),
    )

    try:
        ticket = service.execute(ticket_id)
    except TicketNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return TicketResponse(
        ticket_id=ticket.id,
        cnpj=ticket.cnpj,
        subject=ticket.subject,
        status=ticket.status,
        created_at=ticket.created_at,
    )


@router.patch(
    "/{ticket_id}/close",
    response_model=TicketResponse,
    summary="Fechar Ticket",
)
def close_ticket(
    ticket_id: str,
) -> TicketResponse:
    service = CloseTicketService(
        get_ticket_repository(),
    )

    try:
        ticket = service.execute(ticket_id)
    except TicketNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    return TicketResponse(
        ticket_id=ticket.id,
        cnpj=ticket.cnpj,
        subject=ticket.subject,
        status=ticket.status,
        created_at=ticket.created_at,
    )
