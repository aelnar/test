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

# get commit date
headcommit = repo.head.commit
print(headcommit.committed_date)
print(headcommit.authored_date)
