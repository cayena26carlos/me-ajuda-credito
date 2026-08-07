from app.domain.ticket.repository import TicketRepository
from app.infrastructure.database.supabase import supabase_client
from app.infrastructure.repositories.supabase_ticket_repository import (
    SupabaseTicketRepository,
)


def get_ticket_repository() -> TicketRepository:
    return SupabaseTicketRepository(
        supabase_client,
    )
