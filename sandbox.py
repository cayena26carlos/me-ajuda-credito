from app.application.services.subject_execution_service import (
    SubjectExecutionService,
)
from app.domain.ticket.service import TicketService

ticket_service = TicketService()

ticket = ticket_service.create(
    subject="cliente_em_atraso",
    user_id="U123456",
    channel="C123456",
    thread_ts="1234567890.123456",
)

service = SubjectExecutionService()

response = service.execute(ticket)

print("=" * 50)
print(response)


"""*/Conteudo.vscode
{
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll.ruff": "explicit",
        "source.organizeImports.ruff": "explicit",
    },
    "python.analysis.typeCheckingMode": "basic",
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
}"""
