import configparser
import os

import pandas as pd

from pgdb import PGDatabase

# Путь к файлам
dirname = os.path.dirname(__file__)

# Настраиваем конфиги
config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"), encoding='utf-8')

# В переменные записываем данные из конфига
FOLDER_PATH = config['Files']['FOLDER_PATH']
DATABASE = config["Database"]

# Создаем эксземпляр
database = PGDatabase(
    host=DATABASE["HOST"],
    database=DATABASE["DATABASE"],
    user=DATABASE["USER"],
    password=DATABASE["PASSWORD"],
)

# Получаем список всех файлов в нужной папке
all_files = os.listdir(FOLDER_PATH)
for file in all_files: # Объединяем файлы в переменную
    full_file_path = os.path.join(FOLDER_PATH, file)
    if os.path.exists(full_file_path): # Проверяем существует ли такой файл
        shops_data = pd.read_csv(full_file_path) # Считываем файл в переменную и удаляем его
        os.remove(full_file_path)
        for i, row in shops_data.iterrows(): # Заносим данные в БД
            query = f"insert into sales_shops values ({row['num_shop']}, {row['num_cash_desk']}, '{row['dt']}', '{row['doc_id']}', '{row['item']}', '{row['category']}', {row['amount']}, {row['price']}, {row['discount']})"
            database.post(query)
