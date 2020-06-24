from app.models.modelsDomainTable import *
from app.controller.database import Database

dbHelper = Database()

# Opcoes Tentativa
dbHelper.saveList(OpcaoTentativa, [
    "Não atende o telefone",
    "O usuário não estava em casa",
    "O usuário estava em casa mas não disponível para o atendimento",
    "Recusou o atendimento"
])

# Raca
dbHelper.saveList(Raca, [
    "Negra",
    "Amarela",
    "Branca",
    "Parda",
    "Indígena"
])

# Sexo
dbHelper.saveList(Sexo, [
    "Masculino",
    "Feminino",
    "Não Opinou"
])

# Doencas Cronicas
dbHelper.saveList(DoencaCronica, [
    "Diabetes",
    "Hipertensão",
    "Alzheimer",
    "AIDS",
    "Asma",
    "Bronquite",
    "Câncer",
    "Mal de Parkinson",
    "DPOC (Doença Pulmonar Obstrutiva Crônica)",
    "Artrite ou outras doenças reumáticas",
    "Doença renal Crônica",
    "Hanseníase"
])

# Parentesco
dbHelper.saveList(Parentesco, [
    "Pai/Mãe",
    "Filho/Filha",
    "Enteado/Enteada",
    "Tio/Tia",
    "Sobrinho/Sobrinha",
    "Avô/Avó",
    "Colega/Amigo/Amiga",
    "Marido/Esposa/Namorado/Namorada",
    "Primo/Prima",
    "Outros"
])

# Beneficio Social
dbHelper.saveList(BeneficioSocial, [
    "Aposentadoria para pessoa de baixa renda",
    "Auxílio emergencial",
    "Benefícios eventuais (cesta básica emergencial, vale-Feira, auxílio funeral)",
    "Bolsa Família",
    "BPC ( benefício de prestação continuada)",
    "Carteira do Idoso",
    "CNH social",
    "Facultativo baixa renda",
    "ID Jovem",
    "Isenção para serviço ambulante",
    "Minha casa, minha vida",
    "Programa de erradicação do trabalho infantil- PITI",
    "Passe-livre para pessoa com deficiência",
    "Tarifa social de água",
    "Tarifa social de energia elétrica",
    "Outros.", 
    "Não se insere em nenhum programa ou não recebe benefícíos",
    "Não sabe informar"
])

# Motivos para sair de casa
dbHelper.saveList(MotivoSair, [
    "Ir ao supermercado ou a farmácia",
    "Trabalhar",
    "Ir a banco/caixas eletrônicos",
    "Ir a casa de familiares e amigos",
    "Trabalho voluntário",
    "Ir a consultas médicas/fazer exames diagnósticos/tratamentos",
    "Outros"
])

# Sintomas
dbHelper.saveList(SintomaFamiliar, [
    "Febre",
    "Cansaço",
    "Tosse Seca",
    "Mialgia",
    "Fadiga",
    "Congestão Nasal",
    "Dor de Cabeça",
    "Conjutivite",
    "Dor de Garganta",
    "Diarréia",
    "Perda de Paladar ou Olfato",
    "Erupção Cutânea",
    "Descoloração dos Dedos das Mãos e dos Pés",
    "Não apresentou nenhum sintoma"
])

# Sintomas Familiares
dbHelper.saveList(SintomaFamiliar, [
    "Tosse",
    "Dor de cabeça ou no corpo",
    "Fadiga",
    "Coriza",
    "Dor de garganta",
    "Dificuldade para respirar",
    "Febre",
    "Não apresentou nenhum sintoma"
])

# Indicadores de medicamento
dbHelper.saveList(IndicadorMedicamento, [
    "Médico",
    "Enfermeiro",
    "Vizinho/Familiar/Amigo/Conhecido",
    "Dentista",
    "Tomou por conta própria",
    "Outro"
])

# Orientacoes finais
dbHelper.saveList(OrientacaoFinal, [
    "Encaminhamento para avaliação presencial",
    "Acompanhamento telefônico em 24 horas",
    "Acompanhamento telefônico em 48 horas",
    "Discussão do caso com o supervisor",
    "Contato com o serviço",
    "Outros"
])

# Estrategia de Saude Familiar
dbHelper.saveList(Esf, [
    "ESF 1",
    "ESF 2"
])