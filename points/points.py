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


def update_user_points(**kwargs):
    userid = kwargs['uuid']
    url = f"{POINTS_URI}/customers/{userid}"
    resp = requests.put(url, json=kwargs)
    return resp


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
            "transaction_product_id": str(uuid.uuid4()),
            "transaction_id": data["transaction_id"],
            "product_id": f"{i['id']:0>3} - {i['name']}",
            "product_qtd": 1,
            "points": i["price"]
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
            "transaction_product_id": str(uuid.uuid4()),
            "transaction_id": data["transaction_id"],
            "product_id": f"{i['id']:0>3} - {i['name']} - refound",
            "product_qtd": 1,
            "points": i["price"]
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
        "transaction_product_id": str(uuid.uuid4()),
        "transaction_id": data["transaction_id"],
        "product_id": reward_id,
        "product_qtd": 1,
        "points": 1000
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