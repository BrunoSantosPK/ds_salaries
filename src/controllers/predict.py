import json
import joblib
from flask import request


class ControllerPredict:

    @staticmethod
    def predict(base_path: str) -> str:
        result = {"success": True, "message": ""}

        try:
            body = json.loads(request.data)
            with open(f"{base_path}/data/model.joblib", "rb") as file:
                model = joblib.load(file)

            model_result = model.transform_predict([body])[0]
            print(model_result)
            result["salary"] = model.transform_predict([body])[0]

        except BaseException as e:
            result["success"] = False
            result["message"] = str(e)

        finally:
            return json.dumps(result)