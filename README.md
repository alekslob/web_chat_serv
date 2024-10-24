# Веб-чат
Веб-приложение для общения в режиме реального времени, позволяющее пользователям обмениваться текстовыми сообщениями.

## Запуск проекта
1. Для запуска необходима версия `python v3.7.9` или выше. 
2. Запустите виртуальное окружение 
   ```
   python -m venv venv
   ```
3. Установите зависимости
   ```
   pip install -r requirements.txt
   ```
5. Обновите подмодули
   ```
   git submodule init
   git submodule update
   ```
7. Запустите проект
   ```
   python run.py
   ```
8. Откройте [http://localhost:8000](http://localhost:8000/) в браузере

## Конфигурация
Файл `web_chat.yaml` с настройками проекта соберется при первом запуске.
```
# Настройки сервера 
server_settings:
  # Порт сервера (int)
  port: 8000
  # Время жизни токена (в минутах) (int)
  access_token_lifetime: 30
# Настройки подключения к базе данных 
db_settings:
  # Имя базы данных (str)
  database: webchat
```

## Папка Static
Содержит скомпилированный код [веб-интерфейса](https://github.com/alekslob/web_chat_front). 
## Сторонние модули:
- [Parametrica](https://github.com/FosterToster/parametrica) - Библиотека для работы с конфигурацией проекта.
