import os

repolistholder=[]
os.chdir("/home/engineer/Documents/Python/")
read_file_path = "/home/engineer/Documents/Python/repolist"
repo_target_path = "/home/engineer/Documents/Python/repotarget"
daily_share_divider = "Daily_share_ends_here"
daily_share = 3 # change this to what ever the daily share is 
with open(read_file_path, "r") as readfile:
    repolistholder = readfile.read().split(",")
    print(repolistholder)
    print(repolistholder[0:daily_share])
readfile.close()    
with open(repo_target_path,"w+") as writefile:  
    repo_counter_writefile = 0       
    while repo_counter_writefile < daily_share:
        writefile.writelines(repolistholder[repo_counter_writefile]+"\n")
        repo_counter_writefile += 1
    writefile.writelines(daily_share_divider)    
    writefile.close()

