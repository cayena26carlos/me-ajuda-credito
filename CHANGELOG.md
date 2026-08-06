# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

Este projeto segue o padrão **Keep a Changelog** e utiliza **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Planned

- Persistência dos Tickets
- Integração com Slack
- Consulta por CNPJ
- Integração com Minha Receita
- Histórico de Tickets
- Workflow Engine
- LLM para interpretação de solicitações

---

### Changed - 2026-08-06

- Introduzida a SubjectEngine como responsável pela execução dos Subjects.
- Removido SubjectExecutionService.
- Subjects agora retornam SubjectResult.
- Registry adaptado para SubjectType.


## [0.4.0] - 2026-08-06

### Added

#### Arquitetura

- Reorganização da camada `application/services` por contexto.
- Criação do contexto `tickets`.
- Separação dos serviços de Subjects e Tickets.
- Atualização completa dos imports.

#### Application Services

- `ListTicketsService`
- `GetTicketService`
- `CloseTicketService`

#### API

Novos endpoints:

- `GET /tickets`
- `GET /tickets/{ticket_id}`
- `PATCH /tickets/{ticket_id}/close`

#### Schemas

- `TicketResponse`
- `TicketListResponse`
- `CloseTicketResponse`

#### Documentação

- Atualização completa do Swagger/OpenAPI para gerenciamento de Tickets.

### Changed

- Organização definitiva da camada Application por contexto.
- Consolidação da arquitetura baseada em Domain + Application + API.

### Fixed

- Tratamento de `TicketNotFound` retornando `404 Not Found`.
- Atualização correta do status do Ticket para `CLOSED`.

---

## [0.3.0] - 2026-08-05

### Added

#### Ticket Management

- Consulta de Tickets por ID.
- Listagem de Tickets.
- Encerramento de Tickets.

#### Domain

- Evolução do modelo `Ticket`.
- Enum `TicketStatus`.
- Exceção `TicketNotFound`.

#### Swagger

- Documentação dos endpoints de consulta de Tickets.

### Changed

- Evolução do ciclo de vida dos Tickets.
- Separação entre regras de negócio e camada HTTP.

---

## [0.2.0] - 2026-08-04

### Added

#### Subjects

- Enum `SubjectType`.
- Modelagem inicial dos tipos de atendimento.
- Estrutura para expansão dos novos Subjects.

#### Ticket

- Introdução da entidade `Ticket`.
- Associação do Ticket à execução de um Subject.
- Suporte ao CNPJ como identificador principal do atendimento.

#### Application

- `ExecuteSubjectService`
- `SubjectExecutionService`

#### API

- Endpoint:

```
POST /subjects/execute
```

#### Schemas

- `ExecuteSubjectRequest`
- `ExecuteSubjectResponse`

### Changed

- Padronização do fluxo de abertura de atendimentos.
- Introdução da arquitetura baseada em Application Services.

---

## [0.1.0] - 2026-08-03

### Added

#### Estrutura Inicial

- Inicialização do projeto FastAPI.
- Configuração do Swagger/OpenAPI.
- Organização inicial das camadas da aplicação.
- Estrutura de Domain.
- Estrutura de Application.
- Estrutura da API.

#### Subjects

- Registry de Subjects.
- Interface base para Subjects.
- Primeiro Subject implementado.

#### Qualidade

- Ruff.
- Pre-commit.
- Organização do projeto para GitHub.
- Padronização inicial da arquitetura.

---

## Roadmap

Próximas funcionalidades planejadas:

- Persistência dos Tickets
- Banco de Dados
- Consulta por CNPJ
- Consulta por Usuário
- Consulta por Status
- Integração Slack
- Minha Receita API
- Histórico de Atendimento
- LLM para interpretação automática das solicitações