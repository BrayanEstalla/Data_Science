import mysql.connector


def load(data):
    resultado = 0
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_g7'
    )
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS countryDB (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        country VARCHAR(255),
                        capital VARCHAR(255),
                        population VARCHAR(255),
                        region VARCHAR(255)
                    );
                    """)
    conn.commit()
    
    insert_query = """
                   insert into countryDB(country,capital,population,region)
                   values(%s,%s,%s,%s)
                   """
    cursor.executemany(insert_query,data)
    conn.commit()
    result = cursor.rowcount
    cursor.close()
    conn.close()
    
    return result