import requests

api_endpoint = "https://flow-api.pluralsight.com/ticket-delivery"

def metrics(api_key, team_id=None, date_range=None, include_nested_teams=None, apex_user_id=None, apex_user_id__in=None, project_ids=None, team_id__in = None):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    } 

    api_response = requests.get(
        api_endpoint + "/metrics/",
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)