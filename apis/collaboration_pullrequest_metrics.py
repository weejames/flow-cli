import requests

api_endpoint = "https://flow-api.pluralsight.com/collaboration/pullrequest/metrics/"

def request(api_key, date_range, apex_user_id, apex_user_id__in, team_id, team_id__in, repo_id, repo_id__in, repo_id_not__in, repo_tag_id, repo_tag_id__in, repo_name, include_nested_teams, include_weekly_data, fields, metrics):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    query_params = {}

    if date_range is not None:
        query_params["date_range"] = date_range
    if apex_user_id is not None:
        query_params["apex_user_id"] = apex_user_id
    if apex_user_id__in is not None:
        query_params["apex_user_id__in"] = apex_user_id__in
    if team_id is not None:
        query_params["team_id"] = team_id
    if team_id__in is not None:
        query_params["team_id__in"] = team_id__in
    if repo_id is not None:
        query_params["repo_id"] = repo_id
    if repo_id__in is not None:
        query_params["repo_id__in"] = repo_id__in
    if repo_id_not__in is not None:
        query_params["repo_id_not__in"] = repo_id_not__in
    if repo_tag_id is not None:
        query_params["repo_tag_id"] = repo_tag_id
    if repo_tag_id__in is not None:
        query_params["repo_tag_id__in"] = repo_tag_id__in
    if repo_name is not None:
        query_params["repo_name"] = repo_name
    if include_nested_teams is not None:
        query_params["include_nested_teams"] = include_nested_teams
    if include_weekly_data is not None:
        query_params["include_weekly_data"] = include_weekly_data
    if fields is not None:
        query_params["fields"] = fields
    if metrics is not None:
        query_params["metrics"] = metrics


    api_response = requests.get(
        api_endpoint,
        headers = headers,
        params = query_params
    ) 

    if (api_response.status_code == 200):
        return api_response.json()
    else:
        raise RuntimeError(api_response.text)