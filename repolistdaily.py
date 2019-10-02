import git, github, os, re
os.chdir("/home/engineer/Documents/Python")
#repolistpath = "/home/engineer/Documents/Python/repolistlined" # with "\n"
repolistpath = "/home/engineer/Documents/Python/repolist" # With any splitter
        

file = open(repolistpath,"r")
for line in file:
    fields = line.split(",")
    dailylist = 4
    for n in range(dailylist):
        #print("\n".join(fields) ## used in testing only as an indicator
        #field = fields(1) ## Used for testing as indicator
        print(fields[n])
    print("This list above is todays list")
file.close
