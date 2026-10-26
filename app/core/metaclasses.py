
from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):

    def __new__(mcs, name, bases, namespace):
        namespace.setdefault("created_at", None)
        namespace.setdefault("updated_at", None)

        return super().__new__(mcs, name, bases, namespace)


class BaseModel(metaclass=ModelMeta):

    def __init__(self):
        now = datetime.now()
        self.created_at = now
        self.updated_at = now

    def update_timestamp(self):
        self.updated_at = datetime.now()
