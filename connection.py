import pyodbc

def connection_postgres(driver='PostgreSQL Unicode',server='127.0.0.1',database='db_python',username='postgres',password='p@ssw0rd'):
    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )
        print("Conexão bem sucedida!")
        return conn;
    except pyodbc.Error as e:
        print(f"Erro ao connectar ao PostgreSQL: {str(e)}")
        return None;

def execute_query(query):
    conn = connection_postgres()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            results = cursor.fetchall()
            cursor.close()
            return results
        except pyodbc.Error as e:
            print(f"Erro: {str(e)}")
            return None
        finally:
            conn.close()