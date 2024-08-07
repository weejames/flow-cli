import requests

api_endpoint = "https://flow.pluralsight.com/v3/customer/metrics/code_fundamentals/period_metrics/"

def request(api_key, team_id, team_id__in, start_date, end_date, include_nested_teams, resolution, apex_user_id, apex_user_id__in, repo_id, repo_id__in, repo_id_not__in, repo_tag_id, repo_tag_id__in, repo_name):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {}

    if team_id is not None:
        query_params["team_id"] = team_id
    if team_id__in is not None:
        query_params["team_id__in"] = team_id__in
    if start_date is not None:
        query_params["start_date"] = start_date
    if end_date is not None:
        query_params["end_date"] = end_date
    if include_nested_teams is not None:
        query_params["include_nested_teams"] = include_nested_teams
    if resolution is not None:
        query_params["resolution"] = resolution
    if apex_user_id is not None:
        query_params["apex_user_id"] = apex_user_id
    if apex_user_id__in is not None:
        query_params["apex_user_id__in"] = apex_user_id__in
    if repo_id is not None:
        query_params["repo_id"] = repo_id
    if repo_id__in is not None:
        query_params["repo_id__in"] = repo_id__in
    if repo_tag_id is not None:
        query_params["repo_tag_id"] = repo_tag_id
    if repo_tag_id__in is not None:
        query_params["repo_tag_id__in"] = repo_tag_id__in
    if repo_name is not None:
        query_params["repo_name"] = repo_name
    
    api_response = requests.get(
        api_endpoint,
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)