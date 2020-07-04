from controller.database import Database
from models.modelsDomainTable import *

db = Database()


class Input:
    def __init__(self, name='', type='text', label='', placeholder='', required=False, mask=None, options=None,
                 multiselect=False, outros=False):
        self.name = name
        self.type = type
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.mask = mask
        self.options = options
        self.multiselect = multiselect
        self.outros = outros


# =============== Utils ===============

btn_trash = Input(type='btn_trash')

btn_add = Input(type='btn_add')

# ============ Atendimento ============

tentativas = Input(
    type='select',
    name='tentativas',
    label='Motivos de falha no contato',
    options=db.selectAllData(Tentativa),
    outros=True,
)

has_atendimento = Input(
    type='select',
    name='has_atendimento',
    label='Conseguiu iniciar o atendimento?',
    options=[
        {'value': 'Sim'},
        {'value': 'Não', 'fields': [tentativas]}
    ]
)
# ============== AdmSaude ==============

adm_nome = Input(
    name='nome',
    label='Nome Completo',
    placeholder='Nome do Usuário',
    required=True
)

adm_crm = Input(
    name='crm',
    label='CRM',
    placeholder='CRM do Usuário',
    required=True
)

adm_cpf = Input(
    name='cpf',
    label='CPF',
    placeholder='999.999.999-99',
    mask='999.999.999-99',
    required=True
)

adm_senha = Input(
    name='senha',
    label='Senha',
    type='password'
)

adm_is_supervisor = Input(
    name='is_supervisor',
    label='É administrador?',
    type="checkbox"
)

# ============== Paciente ==============

nome = Input(
    name='nome',
    label='Nome Completo',
    placeholder='Nome do paciente',
    required=True
)

cpf = Input(
    name='cpf',
    label='CPF',
    placeholder='999.999.999-99',
    mask='999.999.999-99',
    required=True
)

telefone = Input(
    name='telefone',
    label='Telefone',
    mask='(99) 99999999?9',
    placeholder='(99) 999999999'
)

endereco = Input(
    name='endereco',
    label='Endereço',
    placeholder='Rua Recife, 32',
)

data_nasc = Input(
    name='data_nasc',
    label='Data de nascimento',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

etnia = Input(
    type='select',
    name='id_etnia',
    label='Etnia',
    required=True,
    options=db.selectAllData(Etnia)
)

genero = Input(
    type='select',
    name='id_genero',
    label='Gênero',
    required=True,
    options=db.selectAllData(Genero)
)

# ============== Doença Cronica ==============

doenca_cronica = Input(
    name='doenca_cronica',
    type='select',
    label='Qual?',
    options=db.selectAllData(DoencaCronica)
)

data_primeiro_sintoma = Input(
    name='data_primeiro_sintoma',
    label='Data de surgimento do primeiro sintoma',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

# ============== Medicamento ==============

medicamento = Input(
    name='medicamento',
    label='Qual?',
    placeholder='Nome do medicamento',
    required=True
)

dose_medicamento = Input(
    name='dose_medicamento',
    label='Como toma?',
    placeholder='Dose, quantidade de vezes ao dia',
    required=True
)

tempo_medicamento = Input(
    name='tempo_medicamento',
    label='Há quanto tempo?',
    placeholder='30 dias',
    required=True
)

indicador_medicamento = Input(
    name='indicador_medicamento',
    type='select',
    label='Quem?',
    options=db.selectAllData(Indicador),
    required=True
)

has_indicador_medicamento = Input(
    name='has_indicador_medicamento',
    type='select',
    label='Alguém indicou?',
    required=True,
    options=[
        {"value": "Sim", "fields": [indicador_medicamento]},
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

has_medicamento = Input(
    name='has_medicamento',
    type='select',
    label='Toma algum medicamento diariamente?',
    required=True,
    options=[
        {
            'value': 'Sim',
            'fields': [
                [
                    medicamento,
                    dose_medicamento,
                    tempo_medicamento,
                    has_indicador_medicamento,
                    btn_trash
                ],
                btn_add
            ],
        },
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

has_doenca_cronica = Input(
    type='select',
    name='has_doenca_cronica',
    label='Apresenta alguma doença crônica?',
    options=[
        {"value": "Sim", "fields": [[doenca_cronica, data_primeiro_sintoma, btn_trash], btn_add]},
        {"value": "Não"},
        {"value": "Não opinou"},
    ]
)

# ============== ESF ==============

# TODO: Preencher as esfs padrões (config_database.py)
estrategia_saude_familiar = Input(
    name='estrategia_saude_familiar',
    type='select',
    multiselect=True,
    label='Qual?',
    options=db.selectAllData(EstrategiaSaudeFamiliar)
)

has_estrategia_saude_familiar = Input(
    name='has_estrategia_saude_familiar',
    type='select',
    label='É acompanhado por alguma Estratégia de Saúde da Família?',
    required=True,
    options=[
        {"value": "Sim", "fields": [estrategia_saude_familiar]},
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

# ============== Domicílio e Auxílios ==============

qnt_comodos = Input(
    name='qnt_comodos',
    label='Quantos cômodos tem a sua casa?',
    mask='9?9',
    required=True,
)

has_agua_encanada = Input(
    name='has_agua_encanada',
    type='select',
    label='Tem acesso a água na torneira de casa?',
    options=[
        {"value": "Sim"},
        {"value": "Não"}
    ]
)

auxilio = Input(
    name='auxilio',
    type='select',
    label='Quais?',
    multiselect=True,
    required=True,
    options=db.selectAllData(BeneficioSocial)
)

has_auxilio = Input(
    name='has_auxilio',
    type='select',
    label='Está recebendo algum auxílio do governo durante esse período da pandemia?',
    required=True,
    options=[
        {"value": "Sim", "fields": [auxilio]},
        {"value": "Não"},
        {"value": "Já pedi mas ainda não recebi"}
    ]
)

# ============== Isolamento domiciliar ==============

parentesco = Input(
    name='parentesco',
    type='select',
    label='Qual a relação?',
    options=db.selectAllData(Parentesco)
)

parentesco_doenca_cronica = Input(
    name='parentesco_doenca_cronica',
    type='select',
    label='Qual?',
    options=db.selectAllData(DoencaCronica)
)

parentesco_data_primeiro_sintoma = Input(
    name='parentesco_data_primeiro_sintoma',
    label='Data primeiro sintoma',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

has_parentesco_doenca_cronica = Input(
    type='select',
    name='has_parentesco_doenca_cronica',
    label='Tem doença crônica?',
    options=[
        {"value": "Sim", "fields": [
            parentesco_doenca_cronica,
            parentesco_data_primeiro_sintoma
        ]},
        {"value": "Não"},
        {"value": "Não opinou"},
    ]
)

gravida = Input(
    name='gravida',
    type='select',
    multiselect=True,
    label='Quem?',
    required=True,
    options=[],
    placeholder='Nome da mulher'
)

has_gravida = Input(
    name='has_gravida',
    type='select',
    required=True,
    label='Há mulheres grávidas?',
    options=[
        {"value": "Sim", "fields": [gravida]},
        {"value": "Não"},
        {"value": "Não há mulheres no domicílio"}
    ]
)

mora_sozinho = Input(
    name='mora_sozinho',
    type='select',
    label='Mora sozinho?',
    required=True,
    options=[
        {"value": "Sim"},
        {
            "value": "Não",
            "fields": [
                [
                    parentesco,
                    has_parentesco_doenca_cronica,
                    btn_trash
                ],
                btn_add,
                has_gravida,
            ]
        }
    ]
)

# ============== Visitas ==============

visita = Input(
    name='visita',
    label='Quem?',
    placeholder='Sua resposta'
)

pq_vista = Input(
    name='pq_visita',
    label='Porquê?',
    placeholder='Sua resposta'
)

recebeu_visita = Input(
    name='recebeu_visita',
    type='select',
    label='Recebeu visitas nos últimos 15 dias?',
    required=True,
    options=[
        {
            "value": "Sim",
            "fields": [[visita, pq_vista, btn_trash], btn_add]
        },
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

# ============== Isolamento domiciliar ==============

isolamento = Input(
    name='isolamento',
    label='Como tem feito esse isolamento?'
)

nao_isolamento = Input(
    name='nao_isolamento',
    label='Porquê?'
)

has_isolamento = Input(
    name='has_isolamento',
    type='select',
    label='Está conseguindo se manter isolado dos demais?',
    required=True,
    options=[
        {"value": "Sim", "fields": [isolamento]},
        {"value": "Não", "fields": [nao_isolamento]}
    ]
)

dias_quarentena = Input(
    name='dias_quarentena',
    label='Há Quantos dias?',
    mask='9?9'
)

motivo_sair = Input(
    name='motivo_sair',
    type='select',
    multiselect=True,
    required=True,
    label='Quais são os motivos para sair de casa?',
    options=db.selectAllData(MotivoSair),
)

mantem_quarentena = Input(
    name='mantem_quarentena',
    type='select',
    label='Você e as pessoas com quem mora estão conseguindo se manter em casa?',
    required=True,
    options=[
        {"value": "Sim", "fields": [dias_quarentena]},
        {"value": "Não", "fields": [motivo_sair]},
        {"label": "Sai só para atividades essenciais (banco, supermercado, etc)."}
    ]
)

estrategiaComprarAlimentos = {
    "name": "motivosSairDeCasa",
    "type": "checkbox",
    "label": "Qual tem sido a(s) estratégia(s) usada para a compra de alimentos/medicamentos para o domicílio?",
    "options": [
        {
            "label": "Ida pessoal ao mercado",
        },
        {
            "label": "Entrega em casa (via whatsapp, sites, aplicativos, etc).",
        },
        {
            "label": "Alguém tem feito as compras e deixado no domicílio",
        },
        {
            "label": "Outros",
            "field": {
                "name": "estrategiaCompraAlimentoField",
                "placeholder": "Placeholder",
            },
        },
    ]
}

cuidadoPessoaSairCasa = {
    "name": "cuidadoPessoaSairCasa",
    "label": "Quais são os cuidados que essa pessoa tem tido ao sair de casa para comprar esses itens? E ao chegar em casa? Ou ao receber os produtos?",
    "hint": "Ouvir o relato e orientar medidas de redução de risco da transmissão ao sair e voltar para casa e higienização dos produtos que vem da rua, considerando o contexto socioeconômico do domicílio. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário.",
    "placeholder": "Sua resposta",
    "required": True
}

dormeMesmaCama = {
    "name": "dormeMesmaCama",
    "type": "radio",
    "label": "O Sr/Srª dorme com alguém na mesma cama?",
    "hint": "Se o usuário responder de vez em quando, perguntar se dormiu com alguém na mesma cama nos últimos 15 dias para escolher a alternativa adequada",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        }
    ]
}

dormeMesmoQuarto = {
    "name": "dormeMesmoQuarto",
    "type": "radio",
    "label": "E no mesmo quarto?",
    "hint": "Se o usuário responder de vez em quando, perguntar se dormiu com alguém na mesmo quarto nos últimos 15 dias para escolher a alternativa adequada",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        }
    ]
}

quemTrabalhaForaDeCasa = {
    "label": "Quem e qual a ocupação?",
    "name": "porqueMantemIsolamento",
    "placeholder": "Sua resposta",
}

cuidadosSairParaTrabalhar = {
    "label": "Quais cuidados têm tomado ao sair para trabalhar? E ao chegar em casa?",
    "name": "cuidadosSairParaTrabalhar",
    "placeholder": "Sua resposta",
    "hint": "Ouvir o relato e orientar medidas de redução de risco da transmissão ao sair e voltar para casa, considerando o contexto socioeconômico do domicílio. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário."
}

alguemTrabalhaForaDeCasa = {
    "name": "alguemTrabalhaForaDeCasa",
    "type": "radio",
    "label": "Algumas das pessoas que mora com você está precisando sair para trabalhar?",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        },
        {
            "label": "Não se aplica, mora sozinho",
            "fields": [
                quemTrabalhaForaDeCasa,
                cuidadosSairParaTrabalhar
            ]
        }
    ],
}

# Visitas


# Sintomas COVID 19

apresentouSintomasCovid19 = {
    "type": "select",
    "multiple": True,
    "name": "apresentouSintomasCovid19",
    "label": "Apresentou algum dos sintomas abaixo nos últimos dias (desde do último atendimento em saúde)?",
    "options": db.selectAllData(Sintoma),
}

apresentouFebreQuantosGraus = {
    "label": "Caso tenha apresentado febre, de quanto (anotar o maior número relatado)?",
    "name": "apresentouFebreQuantosGraus",
    "placeholder": "Sua resposta",
}

qualMedicamentoTomou = {
    "label": "Qual?",
    "name": "qualMedicamentoTomou",
    "placeholder": "Sua resposta",
}

quemIndicouMedicamento = {
    "name": "quemIndicouMedicamento",
    "type": "select",
    "label": "Quem indicou o uso desse medicamento?",
    "required": True,
    "options": db.selectAllData(Indicador),
}

comoTomaMedicamento = {
    "label": "Como está tomando esse(s) medicamento(s)?",
    "hint": "Ouvir o relato e considerando os problemas identificados ou dúvidas, oriente quanto ao uso adequado do medicamentos. Descreva aqui, sucintamente, os problemas identificados, dúvidas e orientações fornecidas.",
    "name": "comoTomaMedicamento",
    "placeholder": "Sua resposta",
}

tomouAlgumMedicamentoProsSintomas = {
    "name": "tomouAlgumMedicamentoProsSintomas",
    "type": "select",
    "label": "Tomou algum medicamento para os sintomas que apresentou?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                qualMedicamentoTomou,
                quemIndicouMedicamento,
                comoTomaMedicamento,
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não se aplica",
        }
    ],
}

quemApresentouSintomas = {
    "label": "Quem?",
    "name": "quemApresentouSintomas",
    "placeholder": "Sua resposta",
}

quaisSintomasApresentou = {
    "type": "select",
    "required": True,
    "multiple": True,
    "name": "quaisSintomasApresentou",
    "label": "Quais sintomas?",
    "options": db.selectAllData(Sintoma)
}

seFebreDeQuanto = {
    "label": "Se febre, de quanto (anotar o maior número relatado)?",
    "name": "seFebreDeQuanto",
    "placeholder": "Sua resposta",
}

linkNotificacao = {
    "label": "Caso alguém da casa tenha apresentado sintomas, clique aqui para abrir a ficha de notificação: (link)",
    "name": "linkNotificacao",
    "placeholder": "Sua resposta",
}

alguemMaisApresentaSintomaEmCasa = {
    "name": "alguemMaisApresentaSintomaEmCasa",
    "type": "select",
    "label": "Alguma outra pessoa da sua residência está apresentando algum sintoma de gripe (febre, tosse, dificuldade de respirar, fadiga, dor no corpo, por exemplo)?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                quemApresentouSintomas,
                quaisSintomasApresentou,
                seFebreDeQuanto,
                linkNotificacao
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não se aplica, mora sozinho",
        }
    ],
}

# Encerramento do Atendimento/Orientações Finais

orientacaoFinal = {
    "type": "select",
    "multiple": True,
    "name": "orientacaoFinal",
    "label": "Orientação final",
    "options": db.selectAllData(OrientacaoFinal),
}

anotarOrientacoes = {
    "label": "Anotar aqui orientações, dúvidas do atendimento ou qualquer outra informação relevante.",
    "name": "anotarOrientacoes",
    "placeholder": "Sua resposta",
}
