version: '3.8'

services:
  web:
    build:
      context: ../
      dockerfile: Dockerfile
    ports:
      - "${PORT:-5000}:5000"
    environment:
      - CONFIG_PATH=/app/configs/config.yaml
    volumes:
      - ../logs:/app/logs
      - ../data:/app/data
    depends_on:
      - redis
      - db

  redis:
    image: "redis:6.2"
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  db:
    image: "postgres:13"
    environment:
      POSTGRES_USER: "nft_user"
      POSTGRES_PASSWORD: "securepassword123"
      POSTGRES_DB: "nft_valuation_db"
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  redis_data:
  postgres_data: