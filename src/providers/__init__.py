import re

from providers import github
from providers import bitbucket

providers = {
    "github.com": github.process_repo,
    "bitbucket.org": bitbucket.process_repo
}

def parse_provider(repo_url):
    match = re.search(r'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)/(.*$)', repo_url)
    if match:
        domain = match.group(1)
        url_path = match.group(2)
    else:
        raise SystemExit(f'ERROR: Repo URL Invalid ({repo_url})')

    if domain in providers:
        return providers[domain], url_path
    else:
        raise SystemExit(f'ERROR: Domain ({domain}) is not a supported provider ({list(providers.keys())}) .')
