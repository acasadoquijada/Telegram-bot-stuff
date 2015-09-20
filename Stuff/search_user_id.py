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
# This function returns the id of the username id (if the username is in
# the data basegiven as the argument.
# (see dict_updater_saver.py for "dict_updater()")
################################################################################
