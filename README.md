# Модуль подготовки новости

Демо-версия веб-приложения для сохранения новостного материала, подготовки новости и прикрепления изображения.

## Стек

- Backend: Python, Django, Django REST Framework
- Frontend: Vue.js, JavaScript
- База данных: PostgreSQL
- Хранение изображений: MEDIA_ROOT

## Запуск PostgreSQL

```powershell
docker compose up -d
```

## Запуск backend

```powershell
cd backend
python manage.py migrate
python manage.py runserver
```

Backend будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

## Запуск frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend будет доступен по адресу:

```text
http://127.0.0.1:5173/
```

## API

- `POST /api/news-materials/` — сохранить новостной материал
- `POST /api/news/` — сохранить подготовленную новость
- `POST /api/news-images/` — прикрепить изображение к новости
