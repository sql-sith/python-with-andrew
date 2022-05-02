"""A simple program to demonstrate usage of the PyGithub package.

These concepts have been stolen, almost in their entirety, and certainly whole-heartedly,
from https://www.thepythoncode.com/article/using-github-api-in-python.
"""
import base64
from getpass import getpass
from pprint import pprint

from github import Github, GithubException, UnknownObjectException
from requests import RequestException, HTTPError, get as request_get
from requests.auth import HTTPBasicAuth


def get_gh_token():
    """Prompts the user for a GitHub personal access token (PAT) and returns it.

    :return:
        gh_pat: string: the PAT for logging into GitHub; None for unauthenticate access.

    """

    gh_auth_banner = '''
| ------------------------------------------------------------------------------- |
| Please supply your GitHub Personal Access Token (PAT).                          |
|                                                                                 |
| If you do not have a PAT, you can continue by just hitting enter. Your session  |
| will be unauthenticated and severely rate-limited. For details, visit:          |
|         https://docs.github.com/en/rest/overview/other-authentication-methods   |
|                                                                                 |
| ------------------------------------------------------------------------------- |
    '''
    print(gh_auth_banner)

    # the "or None" at the end of these statements just changes empty strings
    # to None so that if the user presses ENTER we don't have '' in those fields.
    # it's totally unnecessary since '' is falsey, but it seems cleaner and
    # more pythonic to me to be able to check for None in other parts of the program.
    return getpass("\nPlease enter your PAT (see comments above): ").strip() or None


def get_gh_target_info(gh_token):
    """Ask the user to name a GitHub account and use the requests package to query GitHub for information about it.

    :param   gh_token: string: The personal access token (PAT) for accessing GitHub.
             None if unauthenticated access should be used..
    :return: gh_target_data: AuthenticatedUser: JSON describing the target GitHub
             account by the program named gh_target_name.
    """

    gh_target_banner = '''
| --------------------------------------------------------------------------------------- |
| Please enter the GitHub user name of the "target" - that is, the user whose information |
|     you want to look up.                                                                |
| --------------------------------------------------------------------------------------- |
    '''
    print(gh_target_banner)

    gh_target_name = input("\nEnter a user to look up on GitHub: ")
    url = f"https://api.github.com/users/{gh_target_name}"

    try:
        if gh_token:
            # the PAT is sent as the password.
            auth = HTTPBasicAuth(username=None, password=gh_token)
            gh_target_json = request_get(url, auth=auth)
        else:
            # user did not enter a PAT, so we will use unauthenticated access.
            # this type of access is severely rate-limited.
            gh_target_json = request_get(url)

        gh_target_json.raise_for_status()
        gh_target_data = gh_target_json.json()

    except RequestException as e:
        raise ValueError(f"Call to {url} failed.") from e
    except HTTPError as e:
        raise ValueError(f"Call to {url} failed.") from e

    return gh_target_data


def get_user_repo_collection(gh_target_name: str, gh_token: str):
    """Use the PyGithub (github) package to get information about the repositories owned by gh_target_name.

    :param gh_target_name: the GitHub account whose repos we are discovering
    :param gh_token: the personal access token for accessing GitHub
    :return: PaginatedList[Repository]: the list of repositories owned by gh_target_name
    """

    try:
        if gh_token is None:
            # user did not enter a PAT, so we will use unauthenticated access.
            # unauthenticated access is severely rate-limited.
            g = Github()
        else:
            g = Github(login_or_token=gh_token)
        gh_target = g.get_user(gh_target_name)
    except GithubException as e:
        raise RuntimeError(f"Error while retrieving information for Github user {gh_target_name}.") from e

    try:
        return gh_target.get_repos()
    except GithubException as e:
        raise RuntimeError(f"Error retrieving repositories info for user {gh_target_name}.") from e


def print_repo_info(repo):
    print()

    repo_name_banner = f"| REPOSITORY NAME: {repo.full_name} |"
    repo_name_banner_header_footer = "| " + "-" * (len(repo_name_banner) - 4) + " |"
    print(repo_name_banner_header_footer)
    print(repo_name_banner)
    print(repo_name_banner_header_footer)
    print(f"    Description: {repo.description}")
    print(f"    Date created: {repo.created_at}")
    print(f"    Date of last push: {repo.pushed_at}")
    print(f"    Home Page: {repo.homepage}")
    print(f"    Language: {repo.language}")
    print(f"    Number of forks: {repo.forks}")
    print(f"    Number of stars: {repo.stargazers_count}")

    file_count = 0
    for content in repo.get_contents(""):
        file_count += 1
        if file_count == 1:
            print()
            print("    -----")
            print("    files")
            print("    -----")

        type_info = "(directory)," if content.type == "dir" else f"({content.size} bytes),"
        print(f"    #{file_count:>3}: {content.name} {type_info} last modified on {content.last_modified}.")

    try:
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except UnknownObjectException as e:
        pass


def print_gh_target_info(gh_target_info):
    pprint(gh_target_info, indent=4)


if __name__ == '__main__':

    gh_token = get_gh_token()

    gh_target_info = get_gh_target_info(gh_token)
    print_gh_target_info(gh_target_info)

    gh_target_repo_collection = get_user_repo_collection(gh_target_info["login"], gh_token)
    for repo in gh_target_repo_collection:
        print_repo_info(repo)

    print()
