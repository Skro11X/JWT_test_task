# JWT_test_task

Реализация системы авторизации аунтификации с использованием redis, для реализации черного и белого списка токенов(JWT). 

Система реализованна с помощью DRF в паре с модулем rest_framework_simplejwt. 

# Установка
Клонируйте репозиторий:

```shell
git clone <ссылка на репозиторий>
cd <папка с репозиторием>
```

Убедитесь, что у вас установлены Docker и Docker Compose

Запустите сервисы с помощью Docker Compose: В корневой директории проекта выполните команду:

```shell
docker-compose up -d
```

Это запустит все контейнеры в фоновом режиме.



---
Проект занял 12 часов

Основные эндпоинты предоставляющие возможность создать токен и переместить его в блэклист. (4 часа)

Добавление доступа к контенту по JWT токену из вайтлиста. (3 часа)

Добавление эндпоинта, который показывает пример работы с ролями. Добавление команды init_groups для manage.py, чтобы создавать нужные роли.(4 часа)

Создание docker compose файла(1 часа)