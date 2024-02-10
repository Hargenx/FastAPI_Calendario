# Agendamento de Consultas com FastAPI

### `Descrição:`
Este projeto demonstra como criar um endpoint para agendar consultas em um calendário usando o FastAPI. Ele não inclui a integração com um calendário real, como Google Calendar ou Outlook.

## Requisitos
Python 3.8 ou superior
FastAPI
Pydantic

## Instalação
pip install fastapi pydantic

## Como usar
1. **Inicie o servidor FastAPI:**
    ```python
    uvicorn main:app --port 8000
    ```

2. **Agende uma consulta usando a API:**
    ```python
    curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "nome": "Raphael Mauricio",
        "data": "30/12/2024",
        "hora": "10:00:00",
        "duracao": {
            "minutos": 60
        }
    }' \
    http://localhost:8000/consultas
    ```
    - ou utilize insomina, postman ou outra API Client

3. **Liste todas as consultas agendadas:**
    ```bash
    curl http://localhost:8000/consultas
    ```

4. **Frontend Simples:**

   Para interagir com a aplicação, abra o arquivo `index.html` em um navegador.


## Observações
- Este é um projeto de exemplo e não inclui a integração com um calendário real.
- Você precisa implementar a lógica de verificar a disponibilidade do horário e agendar a consulta no calendário de sua escolha.
- O código pode ser adaptado para atender às suas necessidades específicas.

## Recursos Adicionais

- [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- [Documentação do Pydantic](https://pydantic-docs.helpmanual.io/)
- [Integração do FastAPI com Google Calendar](https://github.com/tiangolo/fastapi/issues/844)
- [Integração do FastAPI com Outlook](https://github.com/tiangolo/fastapi/issues/1044)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)



## Licença

Este projeto está sob a [Licença MIT](LICENSE).