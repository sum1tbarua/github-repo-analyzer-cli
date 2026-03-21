# utils/api_client.py
"""
Handles:
- GitHub API calls
- pagination
- retry logic
"""
import requests, time

BASE_URL = "https://api.github.com/users"

def fetch_repos_page(username, page, per_page=100):
    url = f"{BASE_URL}/{username}/repos"
    params = {
        "page": page,
        "per_page": per_page,
    }
    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                try:
                    data = response.json()
                except ValueError:
                    print("Invalid JSON response")
                    return None
                if not isinstance(data, list):
                    print("Unexpected API response format")
                    return None
                return data
            elif response.status_code >= 500:
                print(f"Server Error: {response.status_code}. Retrying...")
            else:
                print(f"Permanent Error Occurred: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            print("Timeout occurred. Retrying...")
        except requests.exceptions.ConnectionError:
            print("Connection Error Occurred. Retrying...")
        if attempt < MAX_RETRIES - 1:
            delay = 2 ** attempt
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
        print(f"Failed to fetch page {page} after {MAX_RETRIES} attempts.")
    return None


def fetch_all_repos(username):
    page = 1
    all_repos = list()
    while True:
        if page > 100:
            print("Stopping: too many pages")
            break
        data = fetch_repos_page(username, page, 100)
        if data is None:
            return None
        if not data:
            break
        all_repos.extend(data)
        page += 1
    return all_repos
    