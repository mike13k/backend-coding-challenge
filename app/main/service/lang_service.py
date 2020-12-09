import requests
from datetime import date, timedelta


### HELPER FUNCTIONS ###
def	_get_repos_by_lang(lang, repos):
    '''
        Parameters:
            lang (string): language name
            repos (string): list of repositories
        Returns:
            list of repositories developed with 'lang' language
    '''
    
    languge_repos = []
    for repo in repos:
        if repo['language'] == lang:
            temp_repo = {
                "name" : repo['name'],
                "url" : repo['html_url'],
                "owner" : repo['owner']['login'],
                "stars" : repo['stargazers_count']
            }
            languge_repos.append(temp_repo)

    languge_repos.sort(key=_sort_repo_star, reverse=True)

    return languge_repos


### SORT FUNCTIONS ###
def _sort_lang_repo_count(l):
  return l['repo_count']
def _sort_repo_star(s):
  return s['stars']


### API FUNCTIONS ###
def trending_repo_languages():
    '''
        Use github api for fetching most trending repositories based on the number of stars.

        Rretuns : 
            json list of languages:
                language name
                language repo count
                list of repos
                    repo name
                    repo owner
                    repo url
                    repo stars
    '''

    # Get repos from last 30 days
    days_30 = (date.today() - timedelta(days=30))
    url = "https://api.github.com/search/repositories?q=created:>%s&sort=stars&order=desc&per_page=100" %(days_30.strftime("%Y-%m-%d"))
    response_repos = requests.get(url)
    response_repos_json = response_repos.json()

    # Get languages of trending repos
    null_langs = 'Not Languaged'
    languages = { (item['language'] if item['language'] != None else null_langs) for item in response_repos_json['items'] }

    # Form response
    languages_detailed = []
    for language in languages:
        language_repos = _get_repos_by_lang(language if language != null_langs else None, response_repos_json['items'])
        languages_detailed.append({
            "name" : language,
            "repo_count" : len(language_repos),
            "repos" : language_repos
        })

    languages_detailed.sort(key=_sort_lang_repo_count, reverse=True)
    
    return languages_detailed
