import os

def get_api_key(api_key):
    if api_key:
        return api_key
    
    api_key = os.getenv('FLOW_API_KEY')

    if api_key:
        return api_key
    
    raise ValueError("API Key not provided and FLOW_API_KEY environment variable is not set")