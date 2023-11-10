from .models import Base
from engine import base_engine as engine


def create_table():
    Base.metadata.create_all(engine)