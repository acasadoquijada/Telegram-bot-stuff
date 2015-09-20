################################################################################
# has_privileges function
################################################################################

def has_privileges(m):
    dict_updater()
    uname = m.from_user.username
    return int(DBDIC[uname][1])

################################################################################
# This function returns if an user has privileges looking in a dictioanry
# (see dict_updater_saver.py for "dict_updater()")
################################################################################