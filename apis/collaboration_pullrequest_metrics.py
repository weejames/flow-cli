import requests

api_endpoint = "https://flow-api.pluralsight.com/collaboration/pullrequest/metrics/"

def request(api_key, date_range=None, apex_user_id=None, apex_user_id__in=None, 
            team_id=None, team_id__in=None, repo_id=None, repo_id__in=None, 
            repo_id_not__in=None, repo_tag_id=None, repo_tag_id__in=None, 
            repo_name=None, include_nested_teams=None, include_weekly_data=None, 
            fields=None, metrics=None):

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {key: value for key, value in locals().items() if value is not None and key != "api_key"}

    api_response = requests.get(
        api_endpoint,
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)