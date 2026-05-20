import requests
import os

PALANTIR_URI = os.getenv("PALANTIR_URI")

class PalantirClient:
    
    def __init__(self, base_uri=PALANTIR_URI):
        self.base_uri = base_uri


    def get_predict(self, model_name, id_value):
        url = f"{self.base_uri}/predict"

        body = {
            "model_name": model_name,
            "id": id_value
        }

        response = requests.post(url, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            return {}


    def get_fiel_score(self, user_id):
        resp = self.get_predict(model_name="tmw_score_fiel", id_value=user_id)
        score = resp.get("predictions", {}).get(user_id,{}).get("score_fiel", None)
        return score * 100 if score is not None else None

