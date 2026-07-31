from app.domain.subjects.registry import registry
from app.domain.ticket.models import Ticket


def main():
    ticket = Ticket(
        subject="cliente_em_atraso",
        user_id="U123456",
        channel="C123456",
        thread_ts="1753456745.000100",
    )

    subject = registry.get(ticket.subject)

    response = subject.execute(ticket)

    print("=" * 50)
    print("RESPOSTA DO SUBJECT")
    print("=" * 50)
    print(response)


if __name__ == "__main__":
    main()
