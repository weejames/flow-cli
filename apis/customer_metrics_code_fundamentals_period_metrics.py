import requests

api_endpoint = "https://flow.pluralsight.com/v3/customer/metrics/code_fundamentals/period_metrics/"

def request(api_key, team_id=None, team_id__in=None, start_date=None, end_date=None, include_nested_teams=None, resolution=None, apex_user_id=None, apex_user_id__in=None, repo_id=None, repo_id__in=None, repo_id_not__in=None, repo_tag_id=None, repo_tag_id__in=None, repo_name=None):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {
        key: value for key,
        value in locals().items() if value is not None and key != "api_key"
    }
    
    api_response = requests.get(
        api_endpoint,
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)