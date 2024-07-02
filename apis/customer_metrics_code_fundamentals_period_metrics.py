import requests

api_endpoint = "https://flow.pluralsight.com/v3/customer/metrics/code_fundamentals/period_metrics/"

def request(api_key, team_id, start_date, end_date, include_nested_teams, resolution):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        "team_id": team_id,
        "start_date": start_date,
        "end_date": end_date,
        "include_nested_teams": include_nested_teams,
        "resolution": resolution
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