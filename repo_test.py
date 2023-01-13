# fcns from gitpython doc -> https://gitpython.readthedocs.io/en/stable/tutorial.html

import git
import time

# repo.working_tree_dir -> repo link (local)
repo = git.Repo(".", search_parent_directories=True)

# active branch
active_branch = repo.active_branch
print("active branch: " + active_branch.name)

# diff framework -> .index.diff
# gitpython doc -> "A diff between the index and the working tree"
# if there's anything in the list -> a file has been changed but not commited
local_change = False
if len(repo.index.diff(None)) > 0:
    local_change = True
print("local changes: " + str(local_change))

# get commit date using commit object
# headcommit.authored_date -> seconds since epoch
# check if commited date is anywhere within seconds of last week
recent_commit = False
headcommit = repo.head.commit
if (headcommit.authored_date <= headcommit.committed_date <= (headcommit.authored_date + 604800)):
    recent_commit = True
print("recent commit: " + str(recent_commit))

# author name of head commit
rufus = False
if(headcommit.author.name == "Rufus"):
    rufus = True
print("blame Rufus: " + str(rufus))
