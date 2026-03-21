# toolkit/analyzer.py
"""
Handles:
- computation
- return a summary dictionary
"""

def analyze_repos(repos):
    """
    Analyze GitHub repositories and return summary metrics.
    Args:
        repos - list of repositories in dictionary form
    Return:
        A dictionary containing 
        - total repos
        - total stars 
        - average stars
        - top repo
        - top language
    """
    if not repos:
        return {
            "Total Repositories": 0,
            "Total Stars": 0,
            "Average Starts": 0,
            "Top Repository": None,
            "Top Language": None
        }
    
    total_repos = len(repos)
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    average_stars = 0
    if total_repos > 0:
        average_stars = round(total_stars / total_repos, 2)
    top_repo = max(repos, key=lambda r: r.get("stargazers_count", 0))
    language_count_dict = dict()
    
    for repo in repos:
        language = repo.get("language")
        if repo.get("language"):
            language_count_dict[language] = language_count_dict.get(language, 0) + 1
    top_language = None
    if language_count_dict:
        top_language = max(language_count_dict, key=language_count_dict.get)
    
    return_dict = {
        "Total Repositories": total_repos,
        "Total Stars": total_stars,
        "Average Stars": average_stars,
        "Top Repository": top_repo.get("name"),
        "Top Language": top_language
    }
    
    return return_dict
    