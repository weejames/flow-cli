import requests

api_endpoint = "https://flow-api.pluralsight.com/dora/build-release"

def leadtime(api_key, team_id=None, date_range=None, include_nested_teams=None, resolution=None):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    } 

    api_response = requests.get(
        api_endpoint + "/change/lead_time",
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text())

def frequency(api_key, team_id=None, date_range=None, include_nested_teams=None, resolution=None):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    } 

    api_response = requests.get(
        api_endpoint + "/deployment/frequency",
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)
    
def changefailure(api_key, team_id=None, date_range=None, include_nested_teams=None, resolution=None):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    }

    api_response = requests.get(
        api_endpoint + "/incident/change_failure_rate",
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text())
    
def time_to_restore(api_key, team_id=None, date_range=None, include_nested_teams=None, resolution=None  ):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    } 

    api_response = requests.get(
        api_endpoint + "/incident/time_to_restore",
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError("Request failed")
