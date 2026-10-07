FROM python:3.12-slim
# Не создавать .pyc и не буферизовать stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1
WORKDIR /app
# Сначала зависимости — для кеширования слоёв
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Затем код
COPY app/ ./app/
# Непривилегированный пользователь
RUN useradd -m appuser && chown -R appuser /app
USER appuser
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "app:app"]