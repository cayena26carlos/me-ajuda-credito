from pathlib import Path

# ==========================================================
# Bootstrap v1.0
# Me Ajuda Crédito
# ==========================================================

PROJECT_STRUCTURE = {
    "app": {
        "__init__.py": "",
        "main.py": "",
        "api": {
            "__init__.py": "",
            "v1": {
                "__init__.py": "",
                "endpoints": {
                    "__init__.py": "",
                    "health.py": "",
                    "tickets.py": "",
                    "subjects.py": "",
                },
            },
        },
        "application": {"__init__.py": "", "services": {"__init__.py": ""}},
        "config": {"__init__.py": "", "settings.py": ""},
        "domain": {
            "__init__.py": "",
            "ticket": {
                "__init__.py": "",
                "models.py": "",
                "service.py": "",
                "repository.py": "",
                "enums.py": "",
                "exceptions.py": "",
            },
            "subjects": {"__init__.py": ""},
        },
        "infrastructure": {"__init__.py": "", "database.py": "", "logger.py": ""},
        "integrations": {
            "__init__.py": "",
            "slack": {"__init__.py": "", "client.py": "", "events.py": ""},
            "metabase": {"__init__.py": "", "client.py": ""},
            "supabase": {"__init__.py": "", "client.py": ""},
        },
        "shared": {
            "__init__.py": "",
            "constants.py": "",
            "helpers.py": "",
            "utils.py": "",
        },
    },
    "tests": {"__init__.py": ""},
    "docs": {},
    "scripts": {},
    ".github": {"workflows": {}},
    ".vscode": {"settings.json": ""},
    ".env.example": """# Slack
SLACK_BOT_TOKEN=
SLACK_SIGNING_SECRET=

# Supabase
SUPABASE_URL=
SUPABASE_KEY=

# Metabase
METABASE_URL=
METABASE_USERNAME=
METABASE_PASSWORD=
""",
    "README.md": """# Me Ajuda Crédito

API responsável pela automação do canal de atendimento da Mesa de Crédito.

## Stack

- Python
- FastAPI
- Slack
- Supabase
- Metabase

""",
    "requirements.txt": """fastapi
uvicorn
pydantic
pydantic-settings
pytest
""",
}


# ==========================================================
# Templates
# ==========================================================

MAIN_TEMPLATE = """from fastapi import FastAPI

app = FastAPI(
    title="Me Ajuda Crédito",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "Me Ajuda Crédito",
        "status": "running"
    }
"""


HEALTH_TEMPLATE = """from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }
"""


SETTINGS_TEMPLATE = """from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Me Ajuda Crédito"

    class Config:
        env_file = ".env"


settings = Settings()
"""


FILE_TEMPLATES = {
    "app/main.py": MAIN_TEMPLATE,
    "app/api/v1/endpoints/health.py": HEALTH_TEMPLATE,
    "app/config/settings.py": SETTINGS_TEMPLATE,
}


# ==========================================================
# Bootstrap
# ==========================================================


def create_structure(base_path: Path, structure: dict):
    for name, value in structure.items():
        path = base_path / name

        if isinstance(value, dict):
            path.mkdir(parents=True, exist_ok=True)
            print(f"📁 {path}")

            create_structure(path, value)

        else:
            if not path.exists():
                content = FILE_TEMPLATES.get(str(path).replace("\\", "/"), value)

                path.write_text(content, encoding="utf-8")

                print(f"📄 {path}")


# ==========================================================
# Main
# ==========================================================


def main():
    print("=" * 60)
    print("🚀 Me Ajuda Crédito Bootstrap")
    print("=" * 60)

    create_structure(Path("."), PROJECT_STRUCTURE)

    print("\n✅ Projeto inicializado com sucesso!")


if __name__ == "__main__":
    main()
