# Указать базовый образ
FROM node:20

WORKDIR /app

# Подтянуть зависимости нашего приложения
COPY ./package.json ./package.json
COPY ./package-lock.json ./package-lock.json

# Установить библиотеки
RUN npm install

# Скопировать исходники
COPY . .

EXPOSE 8080

# Запустить наше приложение
CMD [ "npm", "run", "serve" ]