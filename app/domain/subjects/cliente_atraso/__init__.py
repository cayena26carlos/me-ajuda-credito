from .subject import ClienteEmAtrasoSubject

__all__ = ["ClienteEmAtrasoSubject"]


""" cliente_atraso/
│
├── __init__.py
├── subject.py        ← Entrada do assunto
├── service.py        ← Regras de negócio
├── repository.py     ← Consultas de dados (quando necessário)
├── template.py       ← Mensagens
├── schema.py         ← Modelos Pydantic
└── tests.py          ← Testes específicos do assunto"""
