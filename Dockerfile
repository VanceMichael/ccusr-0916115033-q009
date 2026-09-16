FROM python:3.13-slim
WORKDIR /app
COPY . .
ENV PORT=8080 DATABASE_PATH=/app/data/app.db
RUN mkdir -p /app/data
CMD ["python","-m","app.server"]
