from fastapi import APIRouter

from app.api.schemas.subjects import (
    ExecuteSubjectRequest,
    ExecuteSubjectResponse,
)
from app.application.services.subjects.execute_subject_service import (
    ExecuteSubjectService,
)

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"],
)

execute_subject_service = ExecuteSubjectService()


@router.post(
    "/execute",
    response_model=ExecuteSubjectResponse,
)
def execute_subject(
    request: ExecuteSubjectRequest,
):
    return execute_subject_service.execute(request)
