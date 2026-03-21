# utils/formatter.py

def print_repos(repos, limit=5):
    if not repos:
        print("No repositories to display.")
        return None
    print("\nREPOSITORIES")
    print("-" * 30)
    for repo in repos[:limit]:
        print(f"Repository Name: {repo.get('name')}")
        print(f"Total Stars: {repo.get('stargazers_count', 0)}")
        print(f"Total Forks: {repo.get('forks_count', 0)}")
        print(f"Language: {repo.get('language')}")
        print(f"URL: {repo.get('html_url')}")
        print("-" * 30)
        
def print_summary(summary):
    if not summary:
        print("No summary available.")
        return None
    print("\nSUMMARY")
    print("-" * 30)
    for key, value in summary.items():
        print(f"{key} = {value}")
    