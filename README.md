# Donor_base - База жертвователей центра поддержки женщин в кризисных ситуациях. 
Ссылка на организацию Гитхаба https://github.com/nko-nzhkc/nko/tree/develop


### Pre-commit
Для минимизации трудностей во время разработки и поддержании высокого качества кода в разработке мы используем 
`pre-commit`. Данный фреймворк позволяет проверить код на соответствие `PEP8`, защитить ветки main и develop от 
непреднамеренного коммита, проверить корректность импортов и наличие trailing spaces.
`Pre-commit` конфигурируется с помощью специального файл `.pre-commit-config.yaml`. Для использования фреймворка его 
необходимо установить, выполнив команду из активированного виртуального окружения:

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
В проекте Celery работает вместе c RabbitMQ, который запускается отдельно в контейнере Docker.

Celery включен в индекс пакетов Python (PyPI), поэтому его можно установить с помощью стандартных инструментов Python,
таких как pip:

```bash
(venv)$ pip install celery
```

В проекте реализовано логирование задач Celery в отдельный файл celery.log, на уровне INFO.

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
SECRET_KEY - Секретный ключ Django-проекта в settings.py.

DEBUG - настройка переменной DEBUG в settings.py

ALLOWED_HOSTS - список разрешённых хостов.

#### БД:

POSTGRES_DB - имя базы данных

POSTGRES_USER - имя пользователя, который будет использоваться для входа в базу данных PostgreSQL.

POSTGRES_PASSWORD - пароль пользователя к базе данных.

DB_HOST - адрес, по которому Django будет соединяться с базой данных.

DB_PORT - порт, по которому Django будет обращаться к базе данных.

#### Сервер:

SSH_KEY - закрытый SSH-ключ от сервера.

SSH_PASSPHRASE - пароль для ssh-ключа.

HOST - адрес хоста (IP-адрес сервера).

HOST_USER - имя пользователя на сервере.

#### Переменные для интеграции с другими сервисами:

UNISENDER_API_KEY - ключ от Unisender.

UNISENDER_SENDER_NAME - имя отправителя рассылочных писем.

DEFAULT_FROM_EMAIL - e-mail, с которого будут отправляться сообщения.

CLOUDPAYMENTS_PUBLIC_ID - public_id из личного кабинета Cloudpayments.

CLOUDPAYMENTS_API_SECRET - API-ключ из личного кабинета Cloudpayments.

CLOUDPAYMENTS_API_TEST_URL - url-эндпоинт для проверки для проверки подключения
к API Cloudpayments.

CLOUDPAYMENTS_SUBSCRIPTION_FIND_URL - url-эндпоинт для проверки подписки пользователя на
рекуррентные платежи Cloudpayments.

TEMPLATE_ID - id шаблона приветственного письма из личного кабинета Unisender заказчика

### Cloudpayment
Интернет-эйквайринг, позволяющий получать платежи онлайн с помощью банковской карты или различными методами быстрой
оплаты.

<details>
    <summary><b>Подробнее о сервисе</b></summary>

```shell
https://cloudpayments.ru/integration
```
</details>

Интеграция с Cloudpayments в проекте включает в себя:
- Настройка API-ключа. Ключ выдается платформой при регистрации, добавлен в настройки проекта.
- Обработка платежей осуществляется засчет ответов API. При успешном платеже, а также при неуспешной попытке платежа 
создается соответствующая запись в базе данных проекта.
- После события создания записи в таблице Пожертвования Cloudpayments, отправляется запрос к API Cloudpayments 
для проверки наличия у плательщика подписки на рекуррентные платежи, с последующим сохранением данных в БД проекта.
- Реализована возможность проверки подключения к API Cloudpayments с помощью тест-кейса Django.

### Письма о новом доноре, подписавшемся на регулярный платеж
При создании объекта модели Cloudpayment и/или Mixplat, проект проверяет наличие подписки на регулярный платеж у донора,
и если донора до этого не было в базе, отправляет плательщику приветственное письмо через Unisender заказчика. 
Шаблон письма в Unisender разработан заказчиком.

### Интеграция с Unisender API
Django-проект donor_base настроен на автоматическую отправку приветственных писем для 
новых доноров, подписавшихся на рекуррентный(периодический) платеж. Так же, при поступлении ответа от  
эквайрингов, проект анализирует статус платежа и присвает Донору один из статусов: "Разовые", "Рекуррентные", 
"Утратившие подписку". Далее, после присвоения определенного статуса, донор переносится в соответствующую группу
пользователей в списках Unisender заказчика. Благодаря данному функционалу реализована основная задача по автоматизации
работы заказчика. Ранее заказчик эту группировку выполнял самостоятельно в ручном режиме, что занимало большее 
количество времени.
Этот функционал реализован через специальный интерфейс для разработчиков Unisender API.
В окружение необходимо установить библиотеку requests.

<details>
    <summary><b>Подробнее о сервисе</b></summary>

```shell
https://www.unisender.com/ru/support/api/common/bulk-email/
```
</details>

Базовые настройки интеграции с Unisender API описаны в конфигурационном файле проекта:
```python
DEFAULT_CONF = {
        "base_url": "https://api.unisender.com",
        "lang": "en",
        'format': 'json',
        "api_key": None,
        'platform': None,
    }
```
Для получения "api_key" потребуется регистрация в сервисе Unisender, сгенерированный ключ станет доступен в настройках 
аккаунта.

Подпапка проекта donor_base это базовая директория нашего проекта. В ней в файле unisender_client.py расположен клиент 
для низкоуровнего доступа к Unisender API. Существующая интеграция реализует метод «import_contacts»:
```python
cl = Client(
    api_key=os.getenv("UNISENDER_API_KEY"),
    platform="donor_base",
)
method = "import_contacts"
data_unisender = {
    "field_names": ["email", "Name", "email_list_ids"],
    "data": [],
    "overwrite_lists": 1,
}
```
Источник импорта контактов модель Contact приложения contacts:
```python
cont = Contact.objects.all()
data = []
for x in cont:
    donor_contact = [x.email, x.username, "Oldest_donors"]
    data.append(donor_contact)
data_unisender["data"] = data
```
[Другие методы Unisender API](https://www.unisender.com/ru/support/api/api)

### Логирование в проекте
Подключено логирование через настройки Django и логирование задач, выполняемых Celery.
Файлы django_info.log и celery.log находятся в директории backend проекта.
Для просмотра логов на сервере необходимо зайти на сервер, далее зайти на работающий контейнер
и читать логи прямо в нем
```shell
cd nko
sudo docker compose -f docker-compose.production.yml exec backend bash
cd nko
cd backend
cat django_info.log
cat celery.log
```
