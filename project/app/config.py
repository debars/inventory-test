# project/config.py

import os


class Config:
    def __init__(self, database_url):
        self.database_url = database_url

    @classmethod
    def from_environ(cls):
        return cls(
            os.environ["DATABASE_URL"],
        )


config = Config.from_environ()
