import requests
import os

def google_search(query, num_results=5):
    api_key = os.getenv("GOOGLE_API_KEY")
    cse_id = os.getenv("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        raise Exception("Missing GOOGLE_API_KEY or GOOGLE_CSE_ID environment variables")

    url = (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={api_key}&cx={cse_id}&q={query}&num={num_results}"
    )

    response = requests.get(url)
    
    # If Google returns error, raise it to see the issue
    response.raise_for_status()

    data = response.json()
    return data.get("items", [])
