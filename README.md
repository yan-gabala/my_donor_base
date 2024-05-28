# nko_nzhkc

### Makefile
Make — одна из базовых утилит Юникса, есть на каждой юниксовой машине.
Чтобы проект на Джанге развернуть на новом сервере, нужно выполнить команд пять-десять.
Утилита Make вполне гибкая и может отследить точно, что нужно пересобрать и при этом не пересобирать лишнее.

<details>
    <summary><b>Make на Windows. Ссылка на статью</b></summary>

```shell
https://thelinuxcode.com/run-makefile-windows/
```
</details>

### Pre-commit
Для минимизации трудностей во время разработки и поддержании высокого качества кода в разработке мы используем `pre-commit`. Данный фреймворк позволяет проверить код на соответствие `PEP8`, защитить ветки main и develop от непреднамеренного коммита, проверить корректность импортов и наличие trailing spaces.
`Pre-commit` конфигурируется с помощью специального файл `.pre-commit-config.yaml`. Для использования фреймворка его необходимо установить, выполнив команду из активированного виртуального окружения:

```bash
(venv)$ pip install pre-commit
```
или 

```bash
(venv)$ pip install -r requirements-dev.txt
```
Для принудительной проверки всех файлов можно выполнить команду:
```bash
(venv)$ pre-commit run --all-files
```
При первом запуске будут скачаны и установлены все необходимые хуки, указанные в конфигурационном файле.

Для автоматической проверки всех файлов необходимо инициализировать фреймворк командой:
```bash
(venv)$ pre-commit install
```

### Celery
Celery включен в индекс пакетов Python (PyPI), поэтому его можно установить с помощью стандартных инструментов Python,
таких как pip:

```bash
(venv)$ pip install celery
```

### RabbitMQ 
Является полнофункционалным, стабильным и надежным и простым в установке. Это отличный выбор для производственной
среды. Подробная информаци об использования RabbitMQ с Celery

<details>
    <summary><b>Использование RabbitMQ.</b></summary>

```shell
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq
```
</details>

Если вы используете Linux, установите RabbitMQ, выполнив эту команду

```bash
$ sudo apt-get install rabbitmq-server
```

Или, если вы хотите запустить его в Docker, выполните следующее:

```bash
$ docker run -d -p 5672:5672 rabbitmq
```

Когда команда завершится, брокер уже будет работать в фоновом режиме и готов переместить для вас сообщения: 
.Starting rabbitmq-server: SUCCESS
Вы можете зайти на этот сайт и найти аналогичные простые инструкции по установке для других платформ,
включая Microsoft Windows:

<details>
    <summary><b>Установка RabbitMQ</b></summary>

```shell
http://www.rabbitmq.com/download.html
```
</details>


### Переменные окружения
В репозиторий добавлены следующие переменные окружения:

#### Настройки Django:
DJANGO_SECRET_KEY - Секретный ключ Django-проекта в settings.py.

DEBUG - настройка переменной DEBUG в settings.py

ALLOWED_HOSTS - список разрешённых хостов.

DEFAULT_FROM_EMAIL - e-mail, прописанный в settings.py, с которого будут отправляться сообщения.

#### БД:

DB_NAME - имя базы данных

DB_USER - имя пользователя, который будет использоваться для входа в базу данных PostgreSQL.

DB_PASSWORD - пароль пользователя к базе данных.

DB_HOST - адрес, по которому Django будет соединяться с базой данных.

DB_PORT -  порт, по которому Django будет обращаться к базе данных.

DB_ENGINE - движок базы данных.

#### Сервер:

SSH_KEY - закрытый SSH-ключ от сервера.

SSH_PASSPHRASE - пароль для ssh-ключа.

HOST - адрес хоста (IP-адрес сервера).

HOST_USER - имя пользователя на сервере.

#### Ключи для интеграции с другими сервисами:

UNISENDER_API_KEY - ключ от Unisender.

CLOUDPAYMENTS_PUBLIC_ID - public_id из личного кабинета Cloudpayments.

CLOUDPAYMENTS_API_SECRET - API-ключ из личного кабинета Cloudpayments.

STRIPE_API_KEY - API-ключ от Stripe.
