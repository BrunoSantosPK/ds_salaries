import json
import pickle
from flask import request


class ControllerPredict:

    @staticmethod
    def predict(base_path: str) -> str:
        result = {"success": True, "message": ""}

        try:
            # Carrega modelos e dados para input da previsão
            with open(f"{base_path}/data/model", "wb") as file:
                model = pickle.load(file)

        except BaseException as e:
            result["success"] = False
            result["message"] = str(e)

        finally:
            return json.dumps(result)