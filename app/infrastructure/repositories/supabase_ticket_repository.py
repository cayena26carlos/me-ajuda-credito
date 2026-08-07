from datetime import datetime
from typing import Any

from app.domain.subjects.enums import SubjectType
from app.domain.ticket.enums import TicketStatus
from app.domain.ticket.models import Ticket
from app.domain.ticket.repository import TicketRepository
from supabase import Client


class SupabaseTicketRepository(TicketRepository):
    """
    Implementação do TicketRepository utilizando Supabase.
    """

    TABLE_NAME = "tickets"

    def __init__(self, client: Client) -> None:
        self._client = client

    def save(self, ticket: Ticket) -> Ticket:
        data = {
            "id": ticket.id,
            "cnpj": ticket.cnpj,
            "subject": ticket.subject.value,
            "user_id": ticket.user_id,
            "channel": ticket.channel,
            "thread_ts": ticket.thread_ts,
            "details": ticket.details,
            "status": ticket.status.value,
            "created_at": ticket.created_at.isoformat(),
        }

        self._client.table(self.TABLE_NAME).upsert(data).execute()

        return ticket

    def find_by_id(self, ticket_id: str) -> Ticket | None:
        response = (
            self._client.table(self.TABLE_NAME).select("*").eq("id", ticket_id).limit(1).execute()
        )

        if not response.data:
            return None

        item = response.data[0]

        if not isinstance(item, dict):
            raise TypeError("Resposta inválida recebida do Supabase.")

        return self._to_domain(item)

    def list_all(self) -> list[Ticket]:
        response = (
            self._client.table(self.TABLE_NAME).select("*").order("created_at", desc=True).execute()
        )

        tickets: list[Ticket] = []

        for item in response.data:
            if not isinstance(item, dict):
                raise TypeError("Resposta inválida recebida do Supabase.")

            tickets.append(self._to_domain(item))

        return tickets

    @staticmethod
    def _to_domain(data: dict[str, Any]) -> Ticket:
        return Ticket(
            id=str(data["id"]),
            cnpj=str(data["cnpj"]),
            subject=SubjectType(str(data["subject"])),
            user_id=str(data["user_id"]),
            channel=str(data["channel"]),
            thread_ts=str(data["thread_ts"]),
            details=str(data["details"]) if data.get("details") is not None else None,
            status=TicketStatus(str(data["status"])),
            created_at=datetime.fromisoformat(str(data["created_at"]).replace("Z", "+00:00")),
        )
