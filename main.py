# main.py
from utils.api_client import fetch_all_repos
from utils.formatter import print_repos, print_summary
from toolkit.analyzer import analyze_repos
from utils.file_handler import export_to_json
from utils.config import GITHUB_TOKEN
import argparse, os

def main():
    parser = argparse.ArgumentParser(
        description="GitHub Repo Analyzer CLI"
    )
    parser.add_argument("--user", required=True)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--export", type=str)

    args = parser.parse_args()
    data = fetch_all_repos(args.user)
    
    if GITHUB_TOKEN:
        print("Using authenticated requests")
    else:
        print("Warning: running without token (limited rate)")
    
    if data is None:
        print("Failed to fetch repository data.")
        return

    if not data:
        print("No repositories found.")
        return
    print_repos(data, args.limit)
    
    if args.summary:
        summary = analyze_repos(data)
        if summary is None:
            print("No summary data found.")
        print_summary(summary)
    
    if args.export:
        export_to_json(data, args.export)
    

if __name__ == "__main__":
    main()

