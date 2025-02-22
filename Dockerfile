FROM python:2.7-slim

COPY ant_movement.py /app/
COPY test_ant_movement.py /app/

WORKDIR /app

# Команда для поддержания работы контейнера
CMD ["tail", "-f", "/dev/null"]
