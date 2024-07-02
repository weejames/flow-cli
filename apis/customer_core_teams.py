import requests

api_endpoint = "https://flow.pluralsight.com/v3/customer/core/teams/"

def request(api_key, parentId, parentIsNull):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        "parent__isnull": parentIsNull,
        "parent": parentId,
    }

    api_response = requests.get(api_endpoint, headers = headers, params = query_params)

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError("Request failed")