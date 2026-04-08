FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pydantic openenv-core

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]