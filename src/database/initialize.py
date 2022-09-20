import pandas as pd
from typing import Tuple, List
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
        success, message = True, "Carga de dados de salário finalizada com sucesso."
        session = get_session()
        
        try:
            dataset = pd.read_csv(f"{base_path}/data/ds_salaries.csv")
            insert: List[Salary] = []

            converter = {
                "experience_level": {
                    "MI": "Júnior",
                    "SE": "Pleno",
                    "EN": "Sênior",
                    "EX": "Especialista"
                },
                "employment_type": {
                    "FT": "Full-time",
                    "CT": "Contrato",
                    "PT": "Meio período",
                    "FL": "Freelancer"
                },
                "company_size": {
                    "L": "Grande",
                    "S": "Pequena",
                    "M": "Média"
                }
            }

            for i in range(0, len(dataset)):
                insert.append(Salary(
                    work_year=int(dataset["work_year"].values[i]),
                    experience_level=converter["experience_level"][dataset["experience_level"].values[i]],
                    employment_type=converter["employment_type"][dataset["employment_type"].values[i]],
                    job_title=dataset["job_title"].values[i],
                    salary_usd=dataset["salary_in_usd"].values[i],
                    employee_residence=dataset["employee_residence"].values[i],
                    remote_ratio=dataset["remote_ratio"].values[i],
                    company_location=dataset["company_location"].values[i],
                    company_size=converter["company_size"][dataset["company_size"].values[i]]
                ))

            session.add_all(insert)
            session.commit()

        except BaseException as e:
            session.rollback()
            success, message = False, str(e)

        finally:
            session.close()
            return success, message
