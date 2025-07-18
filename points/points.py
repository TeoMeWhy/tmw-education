import requests
import os
import uuid

POINTS_URI = os.getenv("POINTS_URI")

def get_user_points(**kwargs):
    url = f"{POINTS_URI}/customers"
    resp = requests.get(url, params=kwargs)
    
    if resp.status_code == 200:
        return resp.json()
    
    else:
        return {}


def create_user_points(**kwargs):
    url = f"{POINTS_URI}/customers"
    resp = requests.post(url, json=kwargs)
    
    if resp.status_code == 201:
        return resp.json()["customer"]
    
    else:
        return resp.json()


def make_rpg_store_transaction(tmw_id, items, buyer=True):
    
    data = {
        "transaction_id":str(uuid.uuid4()),
        "customer_id": tmw_id,
        "points": sum(item["price"] for item in items),
        "system_origin":"cursos",
    }

    data['points'] = -1*data['points'] if buyer else data['points']

    data_items = []

    for i in items:
        data_items.append({
            "id": str(uuid.uuid4()),
            "IdTransaction": data["transaction_id"],
            "CodProduct": f"{i['id']:0>3} - {i['name']}",
            "QtdeProduct": 1,
            "VlProduct": i["price"]
        })

    data["products"] = data_items
    return data


def make_rpg_store_transaction_refound(tmw_id, items):
    data = {
        "transaction_id":str(uuid.uuid4()),
        "customer_id": tmw_id,
        "points": sum(item["price"] for item in items),
        "system_origin":"cursos",
    }

    data_items = []

    for i in items:
        data_items.append({
            "id": str(uuid.uuid4()),
            "IdTransaction": data["transaction_id"],
            "CodProduct": f"{i['id']:0>3} - {i['name']} - refound",
            "QtdeProduct": 1,
            "VlProduct": i["price"]
        })

    data["products"] = data_items
    return data

def make_reward_transaction(tmw_id, reward_ids):
    data = {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": tmw_id,
        "system_origin": "cursos",
        "points": 1000 * len(reward_ids),
    }

    data_items = [{
        "id": str(uuid.uuid4()),
        "IdTransaction": data["transaction_id"],
        "CodProduct": reward_id,
        "QtdeProduct": 1,
        "VlProduct": 1000
    } for reward_id in reward_ids]

    data["products"] = data_items
    return data

def post_transaction(**kwargs):
    url = f"{POINTS_URI}/transactions"
    resp = requests.post(url, json=kwargs)
    
    if resp.status_code == 201:
        return resp.json()
    
    else:
        return resp.json()