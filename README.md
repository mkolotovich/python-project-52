# Python проект - "Менеджер задач"
### Hexlet tests and linter status:
[![Actions Status](https://github.com/mkolotovich/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mkolotovich/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e22bac52ac2c7666f469/maintainability)](https://codeclimate.com/github/mkolotovich/python-project-52/maintainability)

## Описание
Task Manager – система управления задачами, подобная http://www.redmine.org/. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация:
[главная страница](https://cdn2.hexlet.io/store/derivatives/original/9451670938b805cdd8f53b0670aaa8ed.png)
[страница регистрации](https://cdn2.hexlet.io/store/derivatives/original/87467cf025839dd429235846d7082102.png)
[страница задач](https://cdn2.hexlet.io/store/derivatives/original/85dbb6329335628c979000bbe53fefae.png)

## Установка и запуск приложения 
1. Убедитесь, что у вас установлен Python версии 3.10 или выше. В противном случае установите Python версии 3.10 или выше.
2. Создайте файл .env в котором пропишите переменную окружения ROLLBAR_ACCESS_TOKEN которая задаёт токен для ROLLBAR и переменную окружения DATABASE_URL которая задаёт параметры подключения к БД.
3. Установите зависимости в систему командой make build. Запуск приложения осуществляется командой make dev в терминале. Команды make build и make dev необходимо запускать из корневой директории проекта.

Ссылка на деплой - https://task-manager-opgj.onrender.com