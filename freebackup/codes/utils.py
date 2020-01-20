"""工具类"""
import os
import sqlite3
import threading
import time

from config import db_file, sql_file


class Database(object):
    """单例模式的一个数据库"""
    _lock = threading.Lock()

    def __init__(self, db_file=db_file, sql_file=sql_file):
        self.db_file = db_file
        self.sql_file = sql_file
        self.get_database()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Database, '_instance'):
            with Database._lock:
                if not hasattr(Database, '_instance'):
                    Database._instance = object.__new__(cls)
        return Database._instance

    def get_database(self):
        # 如果是首次创建数据需初始化
        if not os.path.isfile(self.db_file):
            db = sqlite3.connect(self.db_file)
            with open(self.sql_file, mode='r', encoding='utf8') as f:
                db.executescript(f.read())
        else:
            db = sqlite3.connect(self.db_file)
        return db


def get_modify_time(file):
    # return timestamp like 1579506512.6218083
    t = os.stat(file).st_mtime
    return t



