from enum import StrEnum


class SubjectType(StrEnum):
    """
    Tipos de atendimento suportados pela Mesa de Crédito.
    """

    MOTIVO_REJEICAO = "motivo_rejeicao"
    CADASTRO_BLOQUEADO = "cadastro_bloqueado"
    SOLICITAR_PRAZO_MAIOR = "solicitar_prazo_maior"
    CLIENTE_EM_ATRASO = "cliente_em_atraso"
    ACEITE_TERMO_USO = "aceite_termo_uso"
    CONSUMO_LIMITE_INDEVIDO = "consumo_limite_indevido"
    ERRO_ANALISE = "erro_analise"
    DISTRIBUIR_LIMITE = "distribuir_limite"
    REMOVER_LIMITE = "remover_limite"
    LIMITE_NAO_APARECE = "limite_nao_aparece"
    OUTRO = "outro"
