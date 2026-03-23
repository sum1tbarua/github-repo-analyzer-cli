# utils/api_client.py
"""
Handles:
- GitHub API calls
- authentication
- rate limit validation
- pagination
- retry logic
"""
import requests, time, os
from utils.config import *
from datetime import datetime

def build_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT
    }
    
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    
    return headers

def extract_rate_limit_info(response):
    limit = response.headers.get("X-RateLimit-Limit")
    remaining = response.headers.get("X-RateLimit-Remaining")
    reset = response.headers.get("X-RateLimit-Reset")
    
    reset_readable = "unknown"
    if reset and str(reset).isdigit():
        reset_readable = datetime.fromtimestamp(int(reset)).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "limit": limit,
        "remaining": remaining,
        "reset": reset_readable
    }

def fetch_repos_page(username, page, per_page=DEFAULT_PER_PAGE):
    url = f"{BASE_URL}/users/{username}/repos"
    params = {
        "page": page,
        "per_page": per_page,
    }
    headers = build_headers()
    if not headers:
        return None
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(
                url,
                headers=headers, 
                params=params, 
                timeout=DEFAULT_TIMEOUT
            )
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
            elif response.status_code == 401:
                print("Authentication failed. Check your GitHub token.")
                return None
            elif response.status_code == 404:
                print(f"User '{username}' not found.")
                return None
            elif response.status_code == 403:
                rate_info = extract_rate_limit_info(response)
                if rate_info["remaining"] == "0":
                    print("Github Rate Limit Exceeded.")
                    print(f"Limit: {rate_info['limit']}")
                    print(f"Remaining: {rate_info['remaining']}")
                    print(f"Reset: {rate_info['reset']}")
                else:
                    print("Forbidden Request by GitHub.")
                return None
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
    