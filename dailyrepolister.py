import git, github, os, re
targetdir = "Put your target folder here"
os.chdir(targetdir)
repolistpath = "/home/engineer/Documents/Python/repolistlined"
with open(repolistpath) as targetfile:
    count = 0
    while count < 3:
        content = targetfile.readline()
        count +=1
        print(content)
        
        
    
    
    
