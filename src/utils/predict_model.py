import numpy as np
from typing import List, Any
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression


class Model:
    def __init__(self, models: List[LinearRegression], encoder: OneHotEncoder) -> None:
        self.__models = models
        self.__encoder = encoder

    def transform_job(self, x: Any) -> Any:
        return self.__encoder.transform(x).toarray()

    def predict(self, x: Any) -> List[float]:
        results= []
        for model in self.__models:
            results.append(list(model.predict(x)))
        results = np.array(results)
        return [np.mean(results[:, i]) for i in range(0, len(x))]

    def transform_predict(self, x: List[dict]) -> List[float]:
        values, ohe = [], []
        for i in range(0, len(x)):
            ohe.append(self.transform_job([[x[i]["job_title"]]])[0])
            values.append([
                x[i]["remote_ratio"],
                self.transform_experience(x[i]["experience_level"]),
                self.transform_employment_type(x[i]["employment_type"]),
                self.transform_company_size(x[i]["company_size"])
            ])
        values, ohe = np.array(values), np.array(ohe)
        nx = np.concatenate((values, ohe), axis=1)
        return self.predict(nx)

    def transform_experience(self, name: str) -> int:
        name = name.upper()
        if name == "JÚNIOR":
            return 1
        elif name == "PLENO":
            return 2
        elif name == "SÊNIOR":
            return 3
        elif name == "ESPECIALISTA":
            return 4
        else:
            return 0

    def transform_employment_type(self, name: str) -> int:
        name = name.upper()
        if name == "FULL-TIME":
            return 4
        elif name == "CONTRATO":
            return 3
        elif name == "MEIO PERÍODO":
            return 2
        elif name == "FREELANCER":
            return 1
        else:
            return 0

    def transform_company_size(self, name: str) -> int:
        name = name.upper()
        if name == "PEQUENA":
            return 1
        elif name == "MÉDIA":
            return 2
        elif name == "GRANDE":
            return 3
        else:
            return 0
