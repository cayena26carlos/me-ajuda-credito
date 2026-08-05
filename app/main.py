from fastapi import FastAPI

from app.api.routers.subjects import router as subjects_router
from app.api.routers.tickets import router as tickets_router

app = FastAPI(
    title="Me Ajuda Crédito",
    description="API para automação do canal de atendimento da Mesa de Crédito.",
    version="1.0.0",
)

print(type(subjects_router))
print(type(tickets_router))

app.include_router(subjects_router)
app.include_router(tickets_router)

print(app.routes)


@app.get("/", tags=["Root"])
def root():
    return {
        "application": "Me Ajuda Crédito",
        "version": "1.0.0",
        "status": "running",
    }


print("===================================")
print("ROTAS REGISTRADAS")
print("===================================")
