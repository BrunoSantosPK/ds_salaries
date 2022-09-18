from src.models.base import Base
from sqlalchemy import Column, Integer, Float, String


class Salary(Base):
    __tablename__ = "ds_salaries"
    id = Column(Integer, primary_key=True)
    work_year = Column(Integer, nullable=False)
    experience_level = Column(String, nullable=False)
    employment_type = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    salary_usd = Column(Float, nullable=False)
    employee_residence = Column(String, nullable=False)
    remote_ratio = Column(Integer, nullable=False)
    company_location = Column(String, nullable=False)
    company_size = Column(String, nullable=False)
