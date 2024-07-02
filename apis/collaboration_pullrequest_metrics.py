import requests

api_endpoint = "https://flow-api.pluralsight.com/collaboration/pullrequest/metrics/"

def request(api_key, team_id, date_range, include_nested_teams):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        "team_id": team_id,
        "date_range": date_range,
        "include_nested_teams": include_nested_teams
    }

    api_response = requests.get(
        api_endpoint,
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError("Request failed")