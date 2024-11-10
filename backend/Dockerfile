FROM python:3.10.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /home/app

# Копируем файл с зависимостями приложения
COPY requirements.txt requirements.txt
# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем исходники
COPY . .

# Запускаем приложение
CMD ["python", "-m", "manage", "runserver" ]
