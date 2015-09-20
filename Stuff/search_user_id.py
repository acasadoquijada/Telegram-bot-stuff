################################################################################
# search_user_id funciton
################################################################################

def search_user_id(user_name):
    dict_updater()
    if user_name in DBDIC:
        return int(DBDIC[user_name][0])
    else:
        return -1

################################################################################
# For this function you need to have a csv file with usernames and its id's
# and a dictionary in witch save them (see dict_updater_saver.py).
# Useridprivs.csv should be like this:
################################################################################

# beginning of the file
"user","id","privileges"
@user1,103832,0
@user2,3829453,0
@user3,8432984,1
# end of file