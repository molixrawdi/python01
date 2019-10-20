import git, os, sys, sh
from github import Github
hostnamesource = "  "
hostnametarget = "  "
localTarnsitionalRepo = "/home/engineer/Documents/Python/Code/GitMigrate"
access_token = "      "
# g = Github(access_token)
gsource = Github(base_url="https://{hostnamesource}/api/v3", login_or_token=access_token)
gtarget = Github(base_url="https://{hostnametarget}/api/v3", login_or_token="access_token")
if os.path.exists(localTarnsitionalRepo) is False:
   os.mkdir(localTarnsitionalRepo)
   currentbarerepo = Reo.init(os.path.join(rw_dir,localTarnsitionalRepo),bare=True)
transitionalrepo = Github.Repo(localTarnsitionalRepo) 
print transitionalrepo.Github.status()
