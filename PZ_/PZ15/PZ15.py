import sqlite3
from sqlite3 import Error

def create_connection():
    """Создание подключения к базе данных"""
    conn = None
    try:
        conn = sqlite3.connect('trading_platform.db')
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """Создание таблицы площадка"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS площадка (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                этаж INTEGER NOT NULL,
                площадь REAL NOT NULL,
                кондиционер BOOLEAN NOT NULL,
                стоимость_аренды REAL NOT NULL
            )
        ''')
        conn.commit()
    except Error as e:
        print(e)

def insert_sample_data(conn):
    """Вставка тестовых данных"""
    try:
        cursor = conn.cursor()
        data = [
            (1, 50.5, True, 25000),
            (1, 45.0, False, 20000),
            (2, 60.0, True, 30000),
            (2, 55.0, True, 28000),
            (3, 70.0, False, 35000)
        ]
        cursor.executemany('''
            INSERT INTO площадка (этаж, площадь, кондиционер, стоимость_аренды)
            VALUES (?, ?, ?, ?)
        ''', data)
        conn.commit()
    except Error as e:
        print(e)

def select_queries(conn):
    """3 операции SELECT"""
    print("\n--- SELECT операции ---")
    
    # 1. Выбрать все площадки с кондиционером
    print("\n1. Площадки с кондиционером:")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM площадка WHERE кондиционер = 1')
    for row in cursor.fetchall():
        print(row)
    
    # 2. Выбрать площадки на 1 этаже
    print("\n2. Площадки на 1 этаже:")
    cursor.execute('SELECT * FROM площадка WHERE этаж = 1')
    for row in cursor.fetchall():
        print(row)
    
    # 3. Выбрать площадки с арендой дешевле 30000
    print("\n3. Площадки с арендой < 30000:")
    cursor.execute('SELECT * FROM площадка WHERE стоимость_аренды < 30000')
    for row in cursor.fetchall():
        print(row)

def update_queries(conn):
    """3 операции UPDATE"""
    print("\n--- UPDATE операции ---")
    
    # 1. Увеличить стоимость аренды на 10% для площадок без кондиционера
    print("\n1. Повышение цены на 10% для площадок без кондиционера")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE площадка 
        SET стоимость_аренды = стоимость_аренды * 1.1 
        WHERE кондиционер = 0
    ''')
    conn.commit()
    print(f"Обновлено {cursor.rowcount} записей")
    
    # 2. Установить кондиционер на площадках 3 этажа
    print("\n2. Установка кондиционера на 3 этаже")
    cursor.execute('''
        UPDATE площадка 
        SET кондиционер = 1 
        WHERE этаж = 3
    ''')
    conn.commit()
    print(f"Обновлено {cursor.rowcount} записей")
    
    # 3. Уменьшить площадь площадки с id=2 на 5 кв.м.
    print("\n3. Уменьшение площади площадки с id=2")
    cursor.execute('''
        UPDATE площадка 
        SET площадь = площадь - 5 
        WHERE id = 2
    ''')
    conn.commit()
    print(f"Обновлено {cursor.rowcount} записей")

def delete_queries(conn):
    """3 операции DELETE"""
    print("\n--- DELETE операции ---")
    
    # 1. Удалить площадки с арендой дороже 30000
    print("\n1. Удаление площадок с арендой > 30000")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM площадка WHERE стоимость_аренды > 30000')
    conn.commit()
    print(f"Удалено {cursor.rowcount} записей")
    
    # 2. Удалить площадки на 1 этаже без кондиционера
    print("\n2. Удаление площадок на 1 этаже без кондиционера")
    cursor.execute('DELETE FROM площадка WHERE этаж = 1 AND кондиционер = 0')
    conn.commit()
    print(f"Удалено {cursor.rowcount} записей")
    
    # 3. Удалить площадку с id=4
    print("\n3. Удаление площадки с id=4")
    cursor.execute('DELETE FROM площадка WHERE id = 4')
    conn.commit()
    print(f"Удалено {cursor.rowcount} записей")
    def main():
    # Создание и подключение к базе данных
     conn = create_connection()
     if conn is not None:
        # Создание таблицы
        create_table(conn)
        
        # Очистка таблицы и вставка тестовых данных
        conn.execute('DELETE FROM площадка')
        insert_sample_data(conn)
        
        # Выполнение операций
        select_queries(conn)
        update_queries(conn)
        select_queries(conn)  # Проверка изменений
        delete_queries(conn)
        select_queries(conn)  # Проверка удалений
        
        # Закрытие соединения
        conn.close()
     else:
        print("Ошибка подключения к базе данных")

    if __name__ == 'main':
      main()