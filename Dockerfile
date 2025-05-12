# Dockerfile
FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential curl && apt-get clean

# Instala Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Define o diretório de trabalho
WORKDIR /app

# Copia o projeto (ajuste se necessário)
COPY pyproject.toml poetry.lock* /app/

# Instala dependências
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copia o restante do código
COPY ./app /app/

# Define o PYTHONPATH para garantir que o Python encontre o módulo 'app'
ENV PYTHONPATH=/app

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
