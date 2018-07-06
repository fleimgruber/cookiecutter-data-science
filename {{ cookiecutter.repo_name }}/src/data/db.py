import sqlalchemy
from sqlalchemy.engine import url


def get_engine_local():
    """Get local DB engine"""
    database = {'drivername': 'postgresql+psycopg2',
                'host': 'localhost',
                'port': '5432',
                'username': 'user',
                'database': 'db'
                }
    engine = sqlalchemy.create_engine(url.URL(**database))
    return engine


def get_engine_remote():
    database = {'drivername': 'postgresql+psycopg2',
                'host': 'remote_host',
                'port': '5432',
                'username': 'user',
                'password': 'pass',
                'database': 'db'
                }
    engine = sqlalchemy.create_engine(url.URL(**database))
    return engine
