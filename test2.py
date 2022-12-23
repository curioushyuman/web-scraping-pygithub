#from github import Github
#access_token = "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"
#g = Github(access_token)
#current_user = g.get_user()
#print(current_user.name)
#print(current_user.bio)

import os
from dotenv import load_dotenv
from github import Github
import pandas as pd
load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))
naija_data = g.get_users()
def tablemaker(search_data):
    f_data = []
    for i in search_data:
        user = g.get_user(login=i.login)
        z = {
            'name': user.name,
            'login': user.login,
            'following': user.following,
            'followers': user.followers,
            'email': user.email,
            'id': user.id,
            'location': user.location,
            'Bio': user.bio,
            'Company': user.company,
            'Blog': user.blog,
            'Url': user.url
        }
        f_data.append(z)
        print(z)
        result = pd.DataFrame(f_data)
    return result

data = tablemaker(naija_data)
df = pd.DataFrame(data).to_csv("data.csv")