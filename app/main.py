from fastapi import FastAPI

from app.api.routers.subjects import router as subjects_router

app = FastAPI(
    title="Me Ajuda Crédito",
    description="API para automação do canal de atendimento da Mesa de Crédito.",
    version="1.0.0",
)

app.include_router(subjects_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "application": "Me Ajuda Crédito",
        "version": "1.0.0",
        "status": "running",
    }
