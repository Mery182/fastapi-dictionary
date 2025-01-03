# FastAPI Dictionary App

FastAPI Dictionary App — это RESTful API, созданный на основе FastAPI, который позволяет управлять глоссарием терминов. Приложение поддерживает CRUD операции (создание, чтение, обновление, удаление) и поиск терминов по ключевому слову.

## Функциональность

- **Получение списка всех терминов**  
  `GET /terms` — возвращает все термины из словаря.

- **Получение информации о термине по ID**  
  `GET /terms/{term_id}` — возвращает информацию о термине по его идентификатору.

- **Поиск терминов по ключевому слову**  
  `GET /terms/search?keyword={keyword}` — возвращает список терминов, содержащих указанное ключевое слово.

- **Добавление нового термина**  
  `POST /terms/{term_id}` — добавляет новый термин с заданным ID.

- **Обновление существующего термина**  
  `PUT /terms/{term_id}` — обновляет данные существующего термина.

- **Удаление термина**  
  `DELETE /terms/{term_id}` — удаляет термин по его ID.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/fastapi-dictionary.git
   cd fastapi-dictionary

## Создайте виртуальное окружение и активируйте его:

1. Клонируйте репозиторий:
  python -m venv venv
  source venv/bin/activate  # Для macOS/Linux
  venv\Scripts\activate     # Для Windows
2. Установите зависимости:
   Копировать код
   pip install fastapi uvicorn
3. Запустите сервер разработки:
uvicorn app:app --reload
