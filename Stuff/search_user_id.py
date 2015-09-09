################################################################################
# search_user_id funciton
################################################################################

def search_user_id(user_name):
    f = open("users-id.csv","rt")
    readstrk = csv.reader(f)
    for k in readstrk:
        USID[k[0]] = k[1]
    if user_name in USID:
        return USID[user_name]
    else:
        return -1

################################################################################
# For this function you need to have a csv file with usernames and its id's
# users-id.csv should be like
################################################################################

# start of file in next line
@user1,2514156
@user2,8482563
@user3,875314
# end of file