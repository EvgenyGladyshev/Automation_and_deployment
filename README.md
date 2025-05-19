# Описание проекта
Проект представляет собой систему для автоматической генерации, обработки и хранения данных о продажах в сети магазинов товаров для дома. Система эмулирует работу реальной кассовой программы и автоматизирует процесс сбора и анализа данных.

В этот репозиторий я включил:
- [Сгенерированные данные вызрузки работы кассовых аппартов](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/data)
- [Скриншоты настройки автоматизации и создания БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/img)
- [DDL-команды на создание таблицы БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/tree/master/sql)
- [Скрипт генерации `csv` файлов](https://github.com/EvgenyGladyshev/Automation_and_deployment/blob/master/generate_sales.py)
- [Скрипт занесения `csv` файлов в БД](https://github.com/EvgenyGladyshev/Automation_and_deployment/blob/master/read_files.py)

# Как запустить скрипт

```
# Создаем виртуальное окружение
python -m venv venv2

# Активируем виртуальное окружение
./venv2/scripts/activate #source venv2/bin/activate для Linux

# Устанавливаем зависимости
pip install -r requirements.txt

# Создаем БД
Для этого достаточно запустить DDL-comands.sql в папке sql, и запустить скрипт создания БД

# Запускаем скрипт генерации csv файлов
python generate_sales.py

# Запускам скрипт занесения csv файлов в БД
python read_files.py
```