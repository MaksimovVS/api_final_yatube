# API_Yatube
## API проекта Yatube от Яндекс.Практикум

### Ключевые моменты
  Доступны все модели Yatube (Post, Group, Comment, Follow)
  Аутентификация по JWT-токену
  Запросы и ответы в формате JSON
  
### Установка
  Клонируйте репозитроий с проектом
  
  ###### git clone git@github.com:MaksimovVS/api_final_yatube.git
  
  В директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
  
  python -m venv venv

  source venv/Scripts/activate

  pip install -r requirements.txt

  Выполните миграции:

  python manage.py migrate

  Для запуска сервера введите команду:
  
  python manage.py runserver
  
  По умолчанию проект запускается на http://127.0.0.1:8000/

  Для просмотра документации, примеров запросов и ответов перейдите на:
  
  http://127.0.0.1:8000/redoc/


### Для создания пользователя отправьте POST запрос на адрес:

http://127.0.0.1:8000/api/v1/users/

{
"username": "string",
"password": "string"
}

Для получения JWT - токена такой же запрос на адрес:

http://127.0.0.1:8000/api/v1/jwt/create/

API вернет JWT-токен в формате:

{
    "refresh": "ХХХХХХХХХХХ",
    "access": "ХХХХХХХХХХХХ"
}

Токен вернётся в поле access, а данные из поля refresh нужны для обновления токена/

### Адреса для обращения к API (GET/POST/(PUT or PATCH)/DELETE):

  http://127.0.0.1:8000/posts/ - Список постов (доступна пагинация)/ создать пост
  
  http://127.0.0.1:8000/posts/id/ - Получить пост по id/ обновить/ удалить
  
  http://127.0.0.1:8000/groups/ - Список групп
  
  http://127.0.0.1:8000/groups/id/ - Получить данные группы по id
  
  http://127.0.0.1:8000/posts/id/comments/  - Список коменнтариев под постом / создать комментарий
  
  http://127.0.0.1:8000/posts/id/comments/id/  - Получить комментарий по id/ обновить/ удалить
  
<<<<<<< HEAD
  http://127.0.0.1:8000/follow/ - Список авторов, на которых подписаны/ подписаться на автора
=======
  http://127.0.0.1:8000/follow/ - Список авторов, на которых подписаны/ подписаться на автора
>>>>>>> c715a0a4d4b3019bea8544a1c26ccc051bc40b2b
