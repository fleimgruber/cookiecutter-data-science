import sqlalchemy
from sqlalchemy.engine import url


def get_engine(db_local=False):
    """Get DB engine"""
    if db_local:
        database = {'drivername': 'postgresql+psycopg2',
                    'host': 'localhost',
                    'port': '5432',
                    'username': 'user',
                    'database': 'db'
                    }
        engine = sqlalchemy.create_engine(url.URL(**database))
    else:
        database = {'drivername': 'postgresql+psycopg2',
                    'host': 'remote_host',
                    'port': '5432',
                    'username': 'user',
                    'password': 'pass',
                    'database': 'db'
                    }
        engine = sqlalchemy.create_engine(url.URL(**database))
    return engine
