################################################################################
# search_user_id funciton
################################################################################
def search_user_id(user_name):
    f = open("users-id.txt", "r")
    users_id = f.read()
    f.close()
    usid = 0
    pos = users_id.find(user_name)
    if pos != -1:
        pos1 = users_id.find(" ", pos)
        pos2 = users_id.find("\n", pos1+1)
        usid = int(users_id[pos1:pos2])
        if usid != 0:
            return usid
    return pos


################################################################################
# For this function you need to have a txt file with usernames and its id's
# users-id.txt should be like
################################################################################

@user1 2514156
@user2 8482563
@user3 875314