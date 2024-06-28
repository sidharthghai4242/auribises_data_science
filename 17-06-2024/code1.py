from datetime import datetime 
"""
Principle of oops:

Github repo: repo name, repo id, repo data(....),repo owner,repo access management ,repo acl
"""

#2. create class of object
# below class represents the objects. It is description of objects

class Github_repo:
    pass

#3. create the real object from class in memory
#below is object construction statement
repo1=Github_repo()
print(repo1)
print(id(repo1))
print(hex(id(repo1)))

repo2=Github_repo()


repo1.repo_name="css"
repo1.repo_id="A1bhhsjs"
repo1.repo_owner="njanjndjnd"
src=['filename']
files=['file1','file2','file3']
repo1.data=[src,files]

repo2.repo_name="css1"
repo2.repo_id="A1bhhsjscdjckndkcnkd"
repo2.repo_owner="njanjndjndscjncncnjnc"
src=[]
files=['file1']
repo2.data=[src,files]
repo2.date_initialized= datetime.now().date()


repo3=repo1

repo3.repo_id="jbvjjjbjbjb"
print("repo1 data")
print(vars(repo1))

del repo1.data
print("repo1 data")
print(vars(repo1))

del repo1

print("repo2 data")
print(vars(repo2))

del repo2.data
print("repo2 data")
print(vars(repo2))

del repo2