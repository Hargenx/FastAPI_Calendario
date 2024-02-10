from datetime import datetime, timedelta, time
from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator

app = FastAPI()

# Configuração CORS para permitir solicitações de qualquer origem (método simples)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DuracaoMinutos(BaseModel):
    minutos: int

    @validator('minutos')
    def valida_duracao(cls, v):
        if v <= 0:
            raise ValueError("Duração deve ser maior que zero")
        return v

class Consulta(BaseModel):
    nome: str
    data: datetime
    hora: time  # Alteração aqui
    duracao: DuracaoMinutos

    @validator('data', pre=True, always=True)
    def parse_data(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y")
        return value

    @validator('hora', pre=True, always=True)
    def parse_hora(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%H:%M:%S").time()
        return value

    @validator('data')
    def verifica_data(cls, v):
        if v <= datetime.utcnow():
            raise ValueError("Data não pode estar no passado")
        return v

    @validator('hora')
    def validar_duracao_e_hora(cls, v, values):
        if 'duracao' in values:
            # Validar a duração antes de acessar 'duracao'
            if values['duracao'].minutos <= 0:
                raise ValueError("Duração inválida")

            # Validar a hora
            if v.hour < values['data'].time().hour:
                raise ValueError("Hora da consulta deve ser posterior à data")

        return v

    @validator('hora')
    def consulta_hora_nao_passado(cls, v, values):
        if 'duracao' in values:
            # Acessar 'duracao' após a validação
            fim_tempo = datetime.combine(datetime.utcnow(), v) + timedelta(minutes=values['duracao'].minutos)
            if fim_tempo <= datetime.utcnow():
                raise ValueError("A consulta já passou")

        return v

# Armazenamento de consultas (substitua por integração com calendário real)
consultas = []

# Endpoint para agendar consulta
@app.post("/consultas", response_model=dict)
async def agendar_consulta(body: Consulta = Body(...)):
    """
    Agendar uma consulta.
    """
    # Validação da duração
    if body.duracao.minutos <= 0:
        raise HTTPException(status_code=400, detail="Duração inválida")

    # Verificação de disponibilidade (substitua por lógica real)
    if any(c['data'] == body.data and c['hora'] == body.hora for c in consultas):
        raise HTTPException(status_code=409, detail="Horário indisponível")

    # Persistir os dados em um banco de dados
    # Exemplo: consulta.save() ou consulta.create()
    consultas.append(body.dict())

    return {"message": "Consulta agendada com sucesso!"}

# Endpoint para listar consultas
@app.get("/consultas", response_model=list)
async def listar_consultas():
    return consultas



'''
O modelo Consulta define os campos necessários para agendar uma consulta.
O endpoint /consultas recebe uma requisição POST com os dados da consulta e valida os dados usando Pydantic.
A função verifica a disponibilidade do horário (substitua por lógica real).
A consulta é agendada (substitua por integração com calendário real).
O endpoint /consultas retorna uma lista com todas as consultas agendadas.

Próximos passos:
Integre o código com um calendário real (Google Calendar, Outlook, etc.).
Implemente autenticação e autorização para proteger os endpoints.
Adicione funcionalidades como cancelamento de consulta, edição de consulta, envio de notificações, etc.
'''