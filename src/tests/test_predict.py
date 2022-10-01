import json
import pytest
import pandas as pd
from src.app import app
from os.path import dirname, abspath


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_predict(client):
    base_path = dirname(dirname(dirname(abspath(__file__))))
    df = pd.read_csv(f"{base_path}/data/test.csv")
    equals = []
    
    for i in range(0, len(df)):
        data = {
            "remote_ratio": int(df["remote_ratio"].values[i]),
            "experience_level": df["experience_level"].values[i],
            "employment_type": df["employment_type"].values[i],
            "company_size": df["company_size"].values[i],
            "job_title": df["job_title"].values[i]
        }
        response = client.post("/predict", json=data)
        predict = json.loads(response.get_data(as_text=True))["salary"]
        equals.append(round(predict) == round(df["predict"].values[i]))
    
    assert False not in equals