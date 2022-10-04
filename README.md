# «Бюджет путешествий»

Эта программа будет управлять гугл-таблицей c расчётом расходов на путешествия используя **API google**.

Задачи данного кода будут следующие:

- авторизоваться в Google Sheets;
- создать таблицу;
- выдать права доступа к таблице;
- провести манипуляции с таблицей: прочитать её, сделать новые записи, удалить.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```python
git clone git@github.com:Skrapivn/google_api_project.git
```

Cоздать и активировать виртуальное окружение:

```python
python -m venv venv
```

```python
 . venv/Scripts/activate
```

Обновить версию ```pip``` и установить зависимости из ```requirements.txt```:

```python
python -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

Необходимо изменить ключи, при необходимости, в файле .env.example и переименовать файл в .env:

```python
EMAIL=example@gmail.com - Ваш email от учетной записи Гугл
```

Далее файл необходимо заполнить согласно полученного Json ключа в Google Cloud Platform создав сервисный аккаунт. <https://console.cloud.google.com/projectselector2/home/dashboard>

И подключить два API - ```Google Drive API``` и ```Google Sheets API```.

```python
TYPE=type
PROJECT_ID=project_id
PRIVATE_KEY_ID=private_key_id
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=xxx.gserviceaccount.com
CLIENT_ID=client_id
AUTH_URI=https://
TOKEN_URI=https://
AUTH_PROVIDER_X509_CERT_URL=https://
CLIENT_X509_CERT_URL=https://
```

Для вывода справки, в которой описаны все возможные аргументы для запуска приложения:

```python
python main.py -h
```

Бюджет путешествий

options:
  -h, --help            show this help message and exit
  -c CREATE, --create CREATE
                        Создать файл - введите "имя, бюджет"
  -cl, --clear_all      Удалить все spreadsheets
  -i ID, --id ID        Указать id spreadsheet
  -ls, --list           Вывести все spreadsheets
  -u UPDATE, --update UPDATE
                        Обновить данные табилицы

### Примеры

Создаем таблицу:

```python
python main.py -c "Греция, 70000"
```

Обновляем последнюю из созданных таблиц:

```python
python main.py -u "Транспорт, Билеты на самолёт, 2, 2000, =2*2000"
```

Если необходимо обновить определенный файл, то необходимо использовать ID документа:

```python
python main.py -i ID_таблицы -u "Транспорт, Билеты на самолёт, 2, 15000, =2*15000"
```

Автор:

[Sergey K.](https://github.com/skrapivn/)
