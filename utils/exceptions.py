class GitHubAPIError(Exception):
    pass

class GitHubAuthError(GitHubAPIError):
    pass

class GitHubRateLimitError(GitHubAPIError):
    pass

class GitHubUnexpectedError(GitHubAPIError):
    pass