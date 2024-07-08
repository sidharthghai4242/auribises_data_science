from session21C import MongoDBHelper
from session21A import User
def main():
    print("Welcome to mongo db helper test app")
    dbhelper=MongoDBHelper()

    # user=User()
    # user.add_details_to_user()
    # document=vars(user)
    # dbhelper.insert(document)
    users=dbhelper.fetch()
    for user in users:
        print(user)
if __name__=='__main__':
    main()
