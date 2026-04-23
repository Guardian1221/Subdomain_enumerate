# Subdomain Enumerator CLI

CLI-утилита для поиска поддоменов домена и вывода их текущих IP-адресов (или `N/A`, если адрес не найден).

## Требования

- Python `3.14+`
- Отсутствие внешних зависимостей(OS)
- Docker (опционально, для запуска в контейнере)

## Активация виртуального окружения

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Проверка стиля

```bash
ruff check .
```

## Запуск Docker

```bash
docker build -t subdomain-cli .
docker run --rm subdomain-cli example.com
docker run --rm subdomain-cli example.com --json
```

## Пример работы программы

```bash
python main.py example.com
```

Пример вывода:

```text
www.example.com: 93.184.216.34
api.example.com: N/A
mail.example.com: N/A
```
