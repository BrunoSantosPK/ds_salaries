import pandas as pd
from typing import Tuple
from src.models.base import Base
from src.models.salary import Salary
from src.database.connection import get_engine, get_session


class Initialize:

    @staticmethod
    def create_database() -> Tuple[bool, str]:
        try:
            Base.metadata.create_all(get_engine())
            return True, "Tabelas criadas com sucesso."
        except BaseException as e:
            return False, str(e)

    @staticmethod
    def drop_database() -> Tuple[bool, str]:
        try:
            Base.metadata.drop_all(get_engine())
            return True, "Tabelas removidas com sucesso."
        except BaseException as e:
            return False, str(e)

    @staticmethod
    def salary_data(base_path: str) -> Tuple[bool, str]:
        pass
