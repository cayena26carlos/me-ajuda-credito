from fastapi import APIRouter

from app.api.schemas.subjects import (
    ExecuteSubjectRequest,
    ExecuteSubjectResponse,
)
from app.application.services.subjects.execute_subject_service import (
    ExecuteSubjectService,
)
from app.infrastructure.dependencies import get_ticket_repository

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
)


@router.post(
    "/execute",
    response_model=ExecuteSubjectResponse,
)
def execute_subject(
    request: ExecuteSubjectRequest,
) -> ExecuteSubjectResponse:
    service = ExecuteSubjectService(
        get_ticket_repository(),
    )

    return service.execute(request)
