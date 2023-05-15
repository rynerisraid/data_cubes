from sqlalchemy import create_engine,text
import os


path = os.getcwd()
print(os.getcwd())
sqlite_path = os.path.join(os.getcwd(),fr'examples\database\northwind.db')
print('sqlite:///{}'.format(sqlite_path))

engine = create_engine('sqlite:///{}'.format(sqlite_path), echo=True)


def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        assert result.all()[0][0] == 'hello world'
        
