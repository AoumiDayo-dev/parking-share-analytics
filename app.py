import sqlite3

def init_db():
    """Создает базу данных и наполняет её тестовыми местами"""
    conn = sqlite3.connect('parking.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parking_spots (
            spot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            spot_number TEXT NOT NULL,
            level INTEGER NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM parking_spots")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO parking_spots (spot_number, level) VALUES (?, ?)",
            [('128', -1), ('129', -1), ('201', -2)]
        )
        conn.commit()
    conn.close()

def check_and_book_spot(spot_id):
    """Имитирует обработку API-запроса и делает выборку из БД"""
    conn = sqlite3.connect('parking.db')
    cursor = conn.cursor()
    cursor.execute("SELECT spot_number, level FROM parking_spots WHERE spot_id = ?", (spot_id,))
    spot = cursor.fetchone()
    
    if spot:
        print(f"--- Ответ API [200 OK] ---")
        print(f"Успех! Бот забронировал для вас место №{spot[0]} на {spot[1]} этаже.")
    else:
        print(f"--- Ответ API [404 Not Found] ---")
        print("Ошибка: Место не найдено. Попробуйте изменить параметры.")
        
    conn.close()
if __name__ == "__main__":
    init_db()
    print("Имитация: Пользователь прислал JSON с запросом spot_id = 1")
    check_and_book_spot(1)
