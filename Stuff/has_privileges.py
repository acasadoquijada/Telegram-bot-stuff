################################################################################
# has_privileges function
################################################################################

def has_privileges(m):
    dict_updater()
    uname = m.from_user.username
    return int(DBDIC[uname][1])

################################################################################
# This function needs a file with @usernames and privileges (0 false, 1 true)
# and a dictionary (see dict_updater_saver.py).
# Useridprivs.svg could be like this:
################################################################################

# beginning of the file
"user","id","privileges"
@user1,103832,0
@user2,3829453,0
@user3,8432984,1
# end of file