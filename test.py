#from github import Github
#access_token = "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"
#g = Github(access_token)
#current_user = g.get_user()
#print(current_user.name)
#print(current_user.bio)

import os
from dotenv import load_dotenv
from github import Github
load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    print(dir(repo))