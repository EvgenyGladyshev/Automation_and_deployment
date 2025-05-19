# Описание проекта

Проект представляет собой систему для автоматической генерации, обработки и хранения данных о продажах в сети магазинов товаров для дома. Система эмулирует работу реальной кассовой программы и автоматизирует процесс сбора и анализа данных

В этот репозиторий я добавил:

- [Сгенерированные `csv` файлы каждой кассы](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/data)
- [Скриншоты автоматизации через crontab и создания БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/img)
- [Скрипт создания БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/sql)
- [Скрипт генерации `csv` файлов](https://github.com/EvgenyGladyshev/Automation_and_deployment/blob/master/generate_sales.py)
- [Скрипт записи данных из `csv` файлов в БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/blob/master/read_files.py)

# Как запустить скрипт

```
# Создаем БД
Для этого достаточно запустить DDL-comands.sql и выполнить скрипт создания БД

# Создаем виртуальное окружение
python -m venv venv2

# Активируем виртуальное окружение
./venv2/scripts/activate # source venv2/bin/activate для Linux

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем скрипт генерации файлов
python generate_sales.py

# Запускам скрипт записи данных в БД
python read_files.py
```