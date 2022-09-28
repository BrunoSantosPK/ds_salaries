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
    df = pd.read_csv(f"{base_path}/data/data_test.csv")
    equals = []
    
    for i in range(0, len(df)):
        data = {
            "volatile_acidity": df["volatile_acidity"].values[i],
            "citric_acid": df["citric_acid"].values[i],
            "free_sulfur_dioxide": df["free_sulfur_dioxide"].values[i],
            "alcohol": df["alcohol"].values[i]
        }
        response = client.post("/predict", json=data)
        predict = json.loads(response.get_data(as_text=True))["quality"]
        equals.append(predict == df["predict"].values[i])
    
    assert False not in equals