from sqlalchemy import create_engine,text
import os


path = os.getcwd()
#print(os.getcwd())
sqlite_path = os.path.join(os.getcwd(),fr'examples\database\northwind.db')
#print('sqlite:///{}'.format(sqlite_path))

engine = create_engine('sqlite:///{}'.format(sqlite_path), echo=True)

'''
    create table
'''
def test_create_table():
    with engine.connect() as conn:
        conn.execute(text("create table if not exists some_table(x int, y int)"))
        conn.commit()
        assert "OK"=="OK"
        
    

'''
    insert 
'''
def test_inert_table():
    with engine.connect() as conn:
        conn.execute(text("drop table if exists some_table"))
        conn.execute(text("create table if not exists some_table(x int, y int)"))
        conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 1}, {"x": 2, "y": 4}],)
        conn.commit()
        assert "OK"=="OK"

'''
    delete
'''

'''

'''